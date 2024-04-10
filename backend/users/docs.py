from drf_yasg import openapi

from users.serializers import CartSerializer, FeaturedProductsSerializer

bad_request = openapi.Response(
    description='bad request',
    schema=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'error': openapi.Schema(type=openapi.TYPE_STRING)
        }
    )
)

not_found = openapi.Response(
    description='object not found',
    schema=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'error': openapi.Schema(type=openapi.TYPE_STRING)
        }
    )
)

cart_success = openapi.Response(
    description='success',
    schema=CartSerializer,
)

featured_success = openapi.Response(
    description='success',
    schema=FeaturedProductsSerializer,
)

cart_auth = [
    openapi.Parameter(
        name='Authorization',
        in_=openapi.IN_HEADER,
        type=openapi.TYPE_STRING,
        description='Bearer token for authentication'
    ),
    openapi.Parameter(
        name='Cart',
        in_=openapi.IN_HEADER,
        type=openapi.TYPE_STRING,
        description='Cart token in headers. Example: "Cart: Token <hash-code>"'
    )
]

featured_auth = [
    openapi.Parameter(
        name='Authorization',
        in_=openapi.IN_HEADER,
        type=openapi.TYPE_STRING,
        description='Bearer token for authentication'
    ),
    openapi.Parameter(
        name='Featured',
        in_=openapi.IN_HEADER,
        type=openapi.TYPE_STRING,
        description='Featured token in headers. Example: "Featured: Token <hash-code>"'
    ),
]

changeable_price = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        'changeable_price': openapi.Schema(type=openapi.TYPE_INTEGER),
    },
    required=[]
)


set_user_data = [
    openapi.Parameter(
        name='Authorization',
        in_=openapi.IN_HEADER,
        type=openapi.TYPE_STRING,
        description='Bearer token for authentication'
    ),
    openapi.Parameter(
        name='User',
        in_=openapi.IN_HEADER,
        type=openapi.TYPE_STRING,
        description='Unregistered user token in headers. Example: "User: Token <hash-code>"'
    )
]

set_user_data_body = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        'first_name': openapi.Schema(type=openapi.TYPE_STRING),
        'second_name': openapi.Schema(type=openapi.TYPE_STRING),
        'last_name': openapi.Schema(type=openapi.TYPE_STRING),
        'phone': openapi.Schema(type=openapi.TYPE_STRING),
    },
    required=['first_name', 'last_name', 'phone']
)
