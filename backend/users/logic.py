from functools import wraps

from django.db.models import Prefetch
from rest_framework import status
from rest_framework.response import Response

from users.models import Cart, FeaturedProducts, CartItem, HashCode
from users.tasks import set_interact


def authorize_cart(view_func):
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        if request.user.is_authenticated:
            try:
                cart = Cart.objects.select_related('user').values('id').get(user=request.user)
                set_interact.delay(cart_id=request.user.cart.id)  # set "last interact" field to now
                return view_func(request, cart['id'], *args, **kwargs)
            except Cart.DoesNotExist:
                return Response({'error': 'cart does not exist'}, status=status.HTTP_404_NOT_FOUND)
        else:
            try:
                hash_code = request.headers.get('Cart').split(' ')[1]
            except AttributeError:
                return Response({'error': 'no token provided'}, status=status.HTTP_401_UNAUTHORIZED)
            try:
                cart = Cart.objects.select_related('hash_code').values('id').get(hash_code__token=hash_code)
                set_interact.delay(cart_id=cart.id)  # set "last interact" field to now
                return view_func(request, cart['id'], *args, **kwargs)
            except Cart.DoesNotExist:
                return Response({'error': 'cart does not exist'}, status=status.HTTP_404_NOT_FOUND)
    return wrapper


def authorize_featured(view_func):
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        if request.user.is_authenticated:
            try:
                featured_id = FeaturedProducts.objects.select_related('user').values('id').get(user=request.user)
                set_interact.delay(featured_id=request.user.featured.id)  # set "last interact" field to now
                return view_func(request, featured_id['id'], *args, **kwargs)
            except FeaturedProducts.DoesNotExist:
                return Response({'error': 'featured products does not exist'}, status=status.HTTP_404_NOT_FOUND)
        else:
            try:
                hash_code = request.headers.get('Featured').split(' ')[1]
            except AttributeError:
                return Response({'error': 'no token provided'}, status=status.HTTP_401_UNAUTHORIZED)
            try:
                featured_id = FeaturedProducts.objects.select_related('hash_code').values('id').get(hash_code__token=hash_code)
                set_interact.delay(featured_id=request.user.featured.id)  # set "last interact" field to now
                return view_func(request, featured_id['id'], *args, **kwargs)
            except FeaturedProducts.DoesNotExist:
                return Response({'error': 'featured products does not exist'}, status=status.HTTP_404_NOT_FOUND)

    return wrapper
