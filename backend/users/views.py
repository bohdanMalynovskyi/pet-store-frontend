from django.db import IntegrityError
from django.db.models import Prefetch
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from users.docs import no_token, not_found, cart_success, bad_request, featured_success, cart_auth, featured_auth
from users.logic import authorize_cart, authorize_featured
from users.models import Cart, CartItem, FeaturedProducts, FeaturedItem
from users.serializers import CartSerializer, FeaturedProductsSerializer


@swagger_auto_schema(method='post',
                     responses={201: openapi.Response(description='Cart created', schema=CartSerializer),
                                400: bad_request, 404: not_found})
@api_view(['POST'])
def create_cart(request):
    """Function to create cart"""
    try:
        if request.user.is_authenticated:
            if hasattr(request.user, 'cart'):
                return Response({'error': 'cart is already exist'}, status=status.HTTP_400_BAD_REQUEST)
            else:
                cart = Cart.objects.create(user=request.user)
        else:
            cart = Cart.objects.create(user=None)
        serializer = CartSerializer(cart)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
    return Response(serializer.data, status=status.HTTP_201_CREATED)


@swagger_auto_schema(method='get', responses={200: cart_success, 401: no_token, 404: not_found},
                     manual_parameters=cart_auth)
@api_view(['GET'])
@authorize_cart
def get_cart(request, cart_id):
    cart = Cart.objects.select_related('hash_code').prefetch_related(
                    Prefetch('cart_items', queryset=CartItem.objects.select_related('product').prefetch_related(
                        'product__changeable_prices', 'product__images')
                    )
                ).get(id=cart_id)
    serializer = CartSerializer(cart)
    return Response(serializer.data, status=status.HTTP_200_OK)


@swagger_auto_schema(method='post', responses={200: cart_success, 401: no_token, 404: not_found},
                     manual_parameters=cart_auth)
@api_view(['POST'])
@authorize_cart
def add_to_cart(request, cart_id, product_pk):
    try:
        cart_item = CartItem.objects.get(product_id=product_pk, cart_id=cart_id)
        cart_item.quantity += 1
        cart_item.save()
    except CartItem.DoesNotExist:
        try:
            CartItem.objects.create(cart_id=cart_id, quantity=1, product_id=product_pk)
        except IntegrityError:
            return Response({'error': 'product does not exist'}, status=status.HTTP_404_NOT_FOUND)
    cart = Cart.objects.select_related('hash_code').prefetch_related(
                    Prefetch('cart_items', queryset=CartItem.objects.select_related('product').prefetch_related(
                        'product__changeable_prices', 'product__images')
                    )
                ).get(id=cart_id)
    serializer = CartSerializer(cart)
    return Response(serializer.data, status=status.HTTP_200_OK)


@swagger_auto_schema(method='post', responses={200: cart_success, 401: no_token, 404: not_found},
                     manual_parameters=cart_auth)
@api_view(['POST'])
@authorize_cart
def decrease_quantity(request, cart_id, product_pk):
    try:
        item = CartItem.objects.get(product_id=product_pk, cart_id=cart_id)
    except CartItem.DoesNotExist:
        return Response({'error': 'cart item does not exist'}, status=status.HTTP_404_NOT_FOUND)
    if item.quantity > 1:
        item.quantity -= 1
        item.save()
    elif item.quantity == 1:
        item.delete()
    cart = Cart.objects.select_related('hash_code').prefetch_related(
                    Prefetch('cart_items', queryset=CartItem.objects.select_related('product').prefetch_related(
                        'product__changeable_prices', 'product__images'))).get(id=cart_id)
    serializer = CartSerializer(cart)
    return Response(serializer.data, status=status.HTTP_200_OK)


@swagger_auto_schema(method='delete', responses={200: cart_success, 401: no_token, 404: not_found},
                     manual_parameters=cart_auth)
@api_view(['DELETE'])
@authorize_cart
def delete_cart_item(request, cart_id, product_pk):
    try:
        item = CartItem.objects.get(product_id=product_pk, cart_id=cart_id)
        item.delete()
    except CartItem.DoesNotExist:
        return Response({'error': 'cart item does not exist'}, status=status.HTTP_404_NOT_FOUND)
    cart = Cart.objects.select_related('hash_code').prefetch_related(
                    Prefetch('cart_items', queryset=CartItem.objects.select_related('product').prefetch_related(
                        'product__changeable_prices', 'product__images')
                    )
                ).get(id=cart_id)
    serializer = CartSerializer(cart)
    return Response(serializer.data, status=status.HTTP_200_OK)


@swagger_auto_schema(method='post', responses={200: cart_success, 401: no_token, 404: not_found},
                     manual_parameters=cart_auth)
@api_view(['POST'])
@authorize_cart
def clear_cart(request, cart_id):
    CartItem.objects.filter(cart_id=cart_id).delete()
    cart = Cart.objects.select_related('hash_code').prefetch_related(
                    Prefetch('cart_items', queryset=CartItem.objects.select_related('product').prefetch_related(
                        'product__changeable_prices', 'product__images')
                    )
                ).get(id=cart_id)
    serializer = CartSerializer(cart)
    return Response(serializer.data, status=status.HTTP_200_OK)


@swagger_auto_schema(method='post',
                     responses={201: openapi.Response(description='Featured products created',
                                                      schema=FeaturedProductsSerializer), 400: bad_request,
                                404: not_found})
@api_view(['POST'])
def create_featured_products(request):
    """Function to create featured products"""
    try:
        if request.user.is_authenticated:
            if hasattr(request.user, 'featured'):
                return Response({'error': 'featured products are already exist'}, status=status.HTTP_400_BAD_REQUEST)
            else:
                featured = FeaturedProducts.objects.create(user=request.user)
        else:
            featured = FeaturedProducts.objects.create(user=None)
        serializer = FeaturedProductsSerializer(featured)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
    return Response(serializer.data, status=status.HTTP_201_CREATED)


@swagger_auto_schema(method='get', responses={200: featured_success, 401: no_token, 404: not_found},
                     manual_parameters=featured_auth)
@api_view(['GET'])
@authorize_featured
def get_featured(request, featured_id):
    featured = FeaturedProducts.objects.select_related('hash_code').prefetch_related(
                    Prefetch('featured_items', queryset=FeaturedItem.objects.select_related('product').prefetch_related(
                        'product__changeable_prices', 'product__images')
                    )
                ).get(id=featured_id)
    serializer = FeaturedProductsSerializer(featured)
    return Response(serializer.data, status=status.HTTP_200_OK)


@swagger_auto_schema(method='post', responses={200: featured_success, 401: no_token, 404: not_found, 400: bad_request},
                     manual_parameters=featured_auth)
@api_view(['POST'])
@authorize_featured
def add_to_featured(request, featured_id, product_pk):
    try:
        FeaturedItem.objects.get(featured_products_id=featured_id, product_id=product_pk)
        return Response({'error': 'item already exist'}, status=status.HTTP_400_BAD_REQUEST)
    except FeaturedItem.DoesNotExist:
        try:
            FeaturedItem.objects.create(featured_products_id=featured_id, product_id=product_pk)
        except IntegrityError:
            return Response({'error': 'product does not exist'}, status=status.HTTP_404_NOT_FOUND)

    featured = FeaturedProducts.objects.select_related('hash_code').prefetch_related(
                    Prefetch('featured_items', queryset=FeaturedItem.objects.select_related('product').prefetch_related(
                        'product__changeable_prices', 'product__images')
                    )
                ).get(id=featured_id)
    serializer = FeaturedProductsSerializer(featured)
    return Response(serializer.data, status=status.HTTP_200_OK)


@swagger_auto_schema(method='delete', responses={200: featured_success, 401: no_token, 404: not_found},
                     manual_parameters=featured_auth)
@api_view(['DELETE'])
@authorize_featured
def delete_featured_item(request, featured_id, product_pk):
    try:
        featured_item = FeaturedItem.objects.get(product_id=product_pk, featured_products_id=featured_id)
        featured_item.delete()
    except FeaturedItem.DoesNotExist:
        return Response({'error': 'featured item does not exist'}, status=status.HTTP_404_NOT_FOUND)
    featured = FeaturedProducts.objects.select_related('hash_code').prefetch_related(
                    Prefetch('featured_items', queryset=FeaturedItem.objects.select_related('product').prefetch_related(
                        'product__changeable_prices', 'product__images')
                    )
                ).get(id=featured_id)
    serializer = FeaturedProductsSerializer(featured)
    return Response(serializer.data, status=status.HTTP_200_OK)


@swagger_auto_schema(method='post', responses={200: featured_success, 401: no_token, 404: not_found},
                     manual_parameters=featured_auth)
@api_view(['POST'])
@authorize_featured
def clear_featured(request, featured_id):
    FeaturedItem.objects.filter(featured_products_id=featured_id).delete()
    featured = FeaturedProducts.objects.select_related('hash_code').prefetch_related(
                    Prefetch('featured_items', queryset=FeaturedItem.objects.select_related('product').prefetch_related(
                        'product__changeable_prices', 'product__images')
                    )
                ).get(id=featured_id)
    serializer = FeaturedProductsSerializer(featured)
    return Response(serializer.data, status=status.HTTP_200_OK)
