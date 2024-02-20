from django.db import IntegrityError
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from users.logic import authorize_cart, authorize_featured
from users.models import Cart, CartItem, FeaturedProducts, FeaturedItem
from users.serializers import CartSerializer, CartItemSerializer, FeaturedProductsSerializer, FeaturedItemSerializer


@api_view(['POST'])
def create_cart(request):
    """Function to create cart"""
    try:
        cart = Cart.objects.create()
        serializer = CartSerializer(cart)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
    return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET'])
@authorize_cart
def get_cart(request, cart):
    serializer = CartSerializer(cart)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['POST'])
@authorize_cart
def add_to_cart(request, cart, product_pk):
    try:
        cart_item = cart.cart_items.get(product_id=product_pk)
        cart_item.quantity += 1
        cart_item.save()
    except CartItem.DoesNotExist:
        CartItem.objects.create(cart_id=cart.id, quantity=1, product_id=product_pk)
    cart.refresh_from_db()
    serializer = CartSerializer(cart)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['POST'])
@authorize_cart
def decrease_quantity(request, cart, product_pk):
    try:
        cart_item = cart.cart_items.get(product_id=product_pk)
    except CartItem.DoesNotExist:
        return Response({'error': 'cart item does not exist'}, status=status.HTTP_404_NOT_FOUND)
    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()
    elif cart_item.quantity == 1:
        cart_item.delete()
    cart.refresh_from_db()
    serializer = CartSerializer(cart)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['POST'])
@authorize_cart
def delete_cart_item(request, cart, product_pk):
    try:
        cart_item = cart.cart_items.get(product_id=product_pk)
    except CartItem.DoesNotExist:
        return Response({'error': 'cart item does not exist'}, status=status.HTTP_404_NOT_FOUND)
    cart_item.delete()
    cart.refresh_from_db()
    serializer = CartSerializer(cart)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['POST'])
@authorize_cart
def clear_cart(request, cart):
    cart.cart_items.all().delete()
    cart.refresh_from_db()
    serializer = CartSerializer(cart)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['POST'])
def create_featured_products(request):
    """Function to create featured products"""
    try:
        featured_products = FeaturedProducts.objects.create()
        serializer = FeaturedProductsSerializer(featured_products)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
    return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET'])
@authorize_featured
def get_featured(request, featured):
    featured.refresh_from_db()
    serializer = FeaturedProductsSerializer(featured)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['POST'])
@authorize_featured
def add_to_featured(request, featured, product_pk):
    try:
        FeaturedItem.objects.create(featured_products_id=featured.id, product_id=product_pk)
        serializer = FeaturedProductsSerializer(featured)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except IntegrityError:
        return Response('product does not exist', status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@authorize_featured
def delete_featured_item(request, featured, product_pk):
    try:
        featured_item = featured.featured_items.get(product_id=product_pk)
    except FeaturedItem.DoesNotExist:
        return Response({'error': 'featured item does not exist'}, status=status.HTTP_404_NOT_FOUND)
    featured_item.delete()
    serializer = FeaturedProductsSerializer(featured)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['POST'])
@authorize_featured
def clear_featured(request, featured):
    featured.featured_items.all().delete()
    serializer = FeaturedProductsSerializer(featured)
    return Response(serializer.data, status=status.HTTP_200_OK)
