from functools import wraps

from django.db.models import Prefetch
from rest_framework import status
from rest_framework.response import Response

from products.models import ProductImages
from users.models import Cart, FeaturedProducts, CartItem, FeaturedItem
from users.tasks import set_interact


def authorize_cart(view_func):
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        if request.user.is_authenticated:
            try:
                cart = Cart.objects.select_related('user').values('id').get(user=request.user)
                set_interact.delay(cart_id=cart['id'])  # set "last interact" field to now
                return view_func(request, cart['id'], *args, **kwargs)
            except Cart.DoesNotExist:
                return Response({'error': 'cart does not exist'}, status=status.HTTP_404_NOT_FOUND)
        else:
            try:
                hash_code = request.headers.get('Cart').split(' ')[1]
                cart = Cart.objects.select_related('hash_code').values('id').get(hash_code__key=hash_code)
                set_interact.delay(cart_id=cart['id'])  # set "last interact" field to now
                return view_func(request, cart['id'], *args, **kwargs)
            except AttributeError:
                return Response({'error': 'Token is not provided'}, status=status.HTTP_401_UNAUTHORIZED)
            except Cart.DoesNotExist:
                return Response({'error': 'Token is invalid'}, status=status.HTTP_400_BAD_REQUEST)

    return wrapper


def authorize_featured(view_func):
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        if request.user.is_authenticated:
            try:
                featured = FeaturedProducts.objects.select_related('user').values('id').get(user=request.user)
                set_interact.delay(featured_id=featured['id'])  # set "last interact" field to now
                return view_func(request, featured['id'], *args, **kwargs)
            except FeaturedProducts.DoesNotExist:
                return Response({'error': 'featured products does not exist'}, status=status.HTTP_404_NOT_FOUND)
        else:
            try:
                hash_code = request.headers.get('Featured').split(' ')[1]
                featured = FeaturedProducts.objects.select_related('hash_code').values('id').get(
                    hash_code__key=hash_code)
                set_interact.delay(featured_id=featured['id'])  # set "last interact" field to now
                return view_func(request, featured['id'], *args, **kwargs)
            except AttributeError:
                return Response({'error': 'Token is not provided'}, status=status.HTTP_401_UNAUTHORIZED)
            except FeaturedProducts.DoesNotExist:
                return Response({'error': 'Token is invalid'}, status=status.HTTP_400_BAD_REQUEST)

    return wrapper


def get_cart(cart_id):
    """This func was made to get rid of repeating cart getting query"""
    cart = Cart.objects.select_related('hash_code', 'user').prefetch_related(
        'cart_items__product__subcategory__product_category__animal_category',
        'cart_items__product__changeable_prices',
        Prefetch('cart_items__product__images', queryset=ProductImages.objects.filter(
            order=1), to_attr='filtered_images')).get(id=cart_id)
    return cart


def get_featured(featured_id):
    """This func was made to get rid of repeating featured getting query"""
    featured = FeaturedProducts.objects.select_related('hash_code', 'user').prefetch_related(
        'featured_items__product__subcategory__product_category__animal_category',
        'featured_items__product__changeable_prices',
        Prefetch('featured_items__product__images', queryset=ProductImages.objects.filter(
            order=1), to_attr='filtered_images')).get(id=featured_id)
    return featured
