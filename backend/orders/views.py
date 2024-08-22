from django.db import transaction
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from backend.settings import NP
from orders.docs import create_order_body
from orders.logic import create_order_from_cart, process_delivery
from orders.models import Order
from orders.serializers import OrderSerializer
from orders.tasks import email_paid_order, email_cancelled_order
from users.docs import bad_request, not_found, cart_auth
from users.logic import authorize_cart, get_cart


class OrderViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Short-circuit the view during schema generation
        if getattr(self, 'swagger_fake_view', False):
            return Order.objects.none()  # Return an empty queryset during schema generation

        # Normal behavior
        if self.request.user.is_authenticated:
            queryset = Order.objects.filter(user=self.request.user).order_by('created_at')
        else:
            queryset = Order.objects.none()

        # Apply additional filters
        is_finished = self.request.query_params.get('is_finished')
        is_cancelled = self.request.query_params.get('is_cancelled')
        is_current = self.request.query_params.get('is_current')

        if is_finished is not None and is_finished.lower() == 'true':
            queryset = queryset.filter(status='received')

        if is_cancelled is not None and is_cancelled.lower() == 'true':
            queryset = queryset.filter(status='cancelled')

        if is_current is not None and is_current.lower() == 'true':
            queryset = queryset.exclude(status__in=('cancelled', 'received', 'returned'))

        return queryset

    @swagger_auto_schema(manual_parameters=[
        openapi.Parameter('is_finished', openapi.IN_QUERY, description="Is order finished", type=openapi.TYPE_BOOLEAN),
        openapi.Parameter('is_cancelled', openapi.IN_QUERY, description="Is order cancelled",
                          type=openapi.TYPE_BOOLEAN),
        openapi.Parameter('is_current', openapi.IN_QUERY, description="Is order current", type=openapi.TYPE_BOOLEAN),
    ])
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)


@swagger_auto_schema(method='post',
                     responses={201: openapi.Response(description='Order created', schema=OrderSerializer),
                                400: bad_request, 404: not_found}, manual_parameters=cart_auth,
                     request_body=create_order_body)
@api_view(['POST'])
@authorize_cart
def create_order(request, cart_id):
    try:
        cart = get_cart(cart_id)
        if len(cart.cart_items.all()) == 0:
            return Response({'error': 'cart must be not empty'}, status=status.HTTP_400_BAD_REQUEST)
        order, checkout_url = create_order_from_cart(cart, request)
        serializer = OrderSerializer(order)
        data = serializer.data
        if checkout_url:
            data['checkout_url'] = checkout_url
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
    return Response(data, status=status.HTTP_201_CREATED)


@swagger_auto_schema(method='post',
                     operation_description="Endpoint not for frontend usage! It is needed to receive callbacks from Fondy")
@api_view(['POST'])
def approve_payment(request):
    if request.data.get('response_status') == 'failure':
        return Response(status=status.HTTP_400_BAD_REQUEST)
    payment_status = request.data.get('order_status')
    order_id = request.data.get('order_id')

    if payment_status == 'approved':
        with transaction.atomic():
            order = Order.objects.get(id=order_id)
            order.status = 'payed'
            merchant_data = request.data.get('merchant_data')
            process_delivery(order, merchant_data=merchant_data)
            order.save()
            email_paid_order.delay(order.id, email=order.email if order.email else order.user.email)
        return Response(status=status.HTTP_200_OK)

    elif payment_status == 'expired' or payment_status == 'declined' or payment_status == 'reversed':
        with transaction.atomic():
            order = Order.objects.get(id=order_id)
            order.status = 'cancelled'
            order.reverse_quantity()
            order.save()
            email_cancelled_order.delay(order.id, email=order.email if order.email else order.user.email)
        return Response(status=status.HTTP_200_OK)

    elif payment_status == 'created' or payment_status == 'processing':
        return Response(status=status.HTTP_400_BAD_REQUEST)


@swagger_auto_schema(method='GET', responses={200: 'Nova Post API response', 400: bad_request})
@api_view(['GET'])
def get_settlement_areas(request):
    try:
        response = NP.address.get_settlement_areas('')
    except Exception:
        return Response({'error': 'some error with NOVA POSHTA API occured'}, status=status.HTTP_400_BAD_REQUEST)

    if response['success']:
        return Response(response['data'], status=status.HTTP_200_OK)
    else:
        return Response(response['errors'], status=status.HTTP_400_BAD_REQUEST)


@swagger_auto_schema(method='GET', responses={200: 'Nova Post API response', 400: bad_request},
                     manual_parameters=[
                         openapi.Parameter('area_ref', openapi.IN_QUERY, type=openapi.TYPE_STRING,
                                           description='Area reference(NP id)')
                     ])
@api_view(['GET'])
def get_settlements(request):
    try:
        area_ref = request.query_params.get('area_ref')
        if not area_ref:
            return Response({'error': '"area_ref" is required'}, status=status.HTTP_400_BAD_REQUEST)
        response = NP.address.get_settlements(area_ref=area_ref, warehouse=True, limit=5000, page=1)
    except KeyError:
        return Response({'error': '"area_ref" is required'}, status=status.HTTP_400_BAD_REQUEST)

    if response['success']:
        return Response(response['data'], status=status.HTTP_200_OK)
    else:
        return Response(response['errors'], status=status.HTTP_400_BAD_REQUEST)


@swagger_auto_schema(method='GET', responses={200: 'Nova Post API response', 400: bad_request},
                     manual_parameters=[
                         openapi.Parameter('settlement_ref', openapi.IN_QUERY, type=openapi.TYPE_STRING,
                                           description='Settlement reference(NP id)'),
                         openapi.Parameter('warehouse_type_ref', openapi.IN_QUERY, type=openapi.TYPE_STRING,
                                           description='Type of warehouse ref(NP id). Optional')
                     ])
@api_view(['GET'])
def get_warehouses(request):
    try:
        settlement_ref = request.query_params.get('settlement_ref')
        warehouse_type_ref = request.query_params.get('warehouse_type_ref', None)
        if not settlement_ref:
            return Response({'error': '"settlement_ref" is required'}, status=status.HTTP_400_BAD_REQUEST)
        response = NP.address.get_warehouses(settlement_ref=settlement_ref, type_of_warehouse_ref=warehouse_type_ref,
                                             limit=5000, page=1)
    except KeyError:
        return Response({'error': '"settlement_ref" is required'}, status=status.HTTP_400_BAD_REQUEST)

    if response['success']:
        return Response(response['data'], status=status.HTTP_200_OK)
    else:
        return Response(response['errors'], status=status.HTTP_400_BAD_REQUEST)


@swagger_auto_schema(method='GET', responses={200: 'Nova Post API response', 400: bad_request})
@api_view(['GET'])
def get_warehouse_types(request):
    try:
        response = NP.address.get_warehouse_types()
    except Exception:
        return Response({'error': 'some error with NOVA POSHTA API occured'}, status=status.HTTP_400_BAD_REQUEST)

    except KeyError:
        return Response({'error': '"settlement_ref" is required'}, status=status.HTTP_400_BAD_REQUEST)

    if response['success']:
        return Response(response['data'], status=status.HTTP_200_OK)
    else:
        return Response(response['errors'], status=status.HTTP_400_BAD_REQUEST)
