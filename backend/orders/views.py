from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from backend.settings import NP
from orders.docs import create_order_body, get_warehouse_body
from orders.logic import create_order_from_cart
from orders.models import Order
from orders.serializers import OrderSerializer
from users.docs import bad_request, not_found, cart_auth
from users.logic import authorize_cart, get_cart


class OrderViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)


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
        order = create_order_from_cart(cart, request)
        serializer = OrderSerializer(order)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
    return Response(serializer.data, status=status.HTTP_201_CREATED)


@swagger_auto_schema(method='POST', responses={200: 'Nova Post API response', 400: bad_request},
                     request_body=get_warehouse_body)
@api_view(['POST'])
def get_warehouse(request):
    try:
        response = NP.address.get_warehouses(city_name=request.data['city_name'],
                                             find_by_string=request.data['find_by_string'])
    except KeyError:
        return Response({'error': '"city_name" and "find_by_string" are required'}, status=status.HTTP_400_BAD_REQUEST)
    if response['success']:
        return Response(response['data'], status=status.HTTP_200_OK)
    else:
        return Response(response['errors'], status=status.HTTP_400_BAD_REQUEST)