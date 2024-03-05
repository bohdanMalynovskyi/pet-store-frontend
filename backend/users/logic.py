from functools import wraps

from rest_framework import status
from rest_framework.response import Response

from users.models import Cart, FeaturedProducts
from users.tasks import set_interact


def authorize_cart(view_func):
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        if request.user.is_authenticated:
            try:
                cart = request.user.cart
                set_interact.delay(cart_id=request.user.cart.id)  # set "last interact" field to now
                return view_func(request, cart, *args, **kwargs)
            except Cart.DoesNotExist:
                return Response({'error': 'cart does not exist'}, status=status.HTTP_404_NOT_FOUND)
        else:
            try:
                hash_code = request.headers.get('Cart').split(' ')[1]
            except AttributeError:
                return Response({'error': 'no token provided'}, status=status.HTTP_400_BAD_REQUEST)
            try:
                cart = Cart.objects.get(hash_code=hash_code)
                set_interact.delay(cart_id=cart.id)  # set "last interact" field to now
                return view_func(request, cart, *args, **kwargs)
            except Cart.DoesNotExist:
                return Response({'error': 'cart does not exist'}, status=status.HTTP_404_NOT_FOUND)

    return wrapper


def authorize_featured(view_func):
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        if request.user.is_authenticated:
            try:
                featured = request.user.featured
                set_interact.delay(featured_id=request.user.featured.id)  # set "last interact" field to now
                return view_func(request, featured, *args, **kwargs)
            except FeaturedProducts.DoesNotExist:
                return Response({'error': 'featured products does not exist'}, status=status.HTTP_404_NOT_FOUND)
        else:
            try:
                hash_code = request.headers.get('Featured').split(' ')[1]
            except AttributeError:
                return Response({'error': 'no token provided'}, status=status.HTTP_400_BAD_REQUEST)
            try:
                featured = FeaturedProducts.objects.get(hash_code=hash_code)
                set_interact.delay(featured_id=request.user.featured.id)  # set "last interact" field to now
                return view_func(request, featured, *args, **kwargs)
            except Cart.DoesNotExist:
                return Response({'error': 'featured products does not exist'}, status=status.HTTP_404_NOT_FOUND)

    return wrapper
