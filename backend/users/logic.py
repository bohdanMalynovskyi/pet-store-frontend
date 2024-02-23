from functools import wraps

from rest_framework import status
from rest_framework.response import Response

from users.models import Cart, FeaturedProducts
from users.tasks import set_interact


def authorize_cart(view_func):
    @wraps(view_func)
    def wrapper(request, cart_pk, *args, **kwargs):
        try:
            hash_code = request.headers.get('Authorization').split(' ')[1]
        except AttributeError:
            return Response({'error': 'no token provided'}, status=status.HTTP_400_BAD_REQUEST)
        try:
            cart = Cart.objects.get(id=cart_pk)
            if cart.hash_code == hash_code:
                set_interact.delay(cart_id=cart.id)  # set "last interact" field to now
                return view_func(request, cart, *args, **kwargs)
            else:
                return Response({'error': 'cart not found'}, status=status.HTTP_404_NOT_FOUND)
        except Cart.DoesNotExist:
            return Response({'error': 'cart does not exist'}, status=status.HTTP_404_NOT_FOUND)

    return wrapper


def authorize_featured(view_func):
    @wraps(view_func)
    def wrapper(request, featured_pk, *args, **kwargs):
        try:
            hash_code = request.headers.get('Authorization').split(' ')[1]
        except AttributeError:
            return Response({'error': 'no token provided'}, status=status.HTTP_400_BAD_REQUEST)
        try:
            featured = FeaturedProducts.objects.get(id=featured_pk)
            if featured.hash_code == hash_code:
                set_interact.delay(featured_od=featured.id)  # set "last interact" field to now
                return view_func(request, featured, *args, **kwargs)
            else:
                return Response({'error': 'featured products not found'}, status=status.HTTP_404_NOT_FOUND)
        except FeaturedProducts.DoesNotExist:
            return Response({'error': 'featured products does not exist'}, status=status.HTTP_404_NOT_FOUND)

    return wrapper
