from drf_yasg import openapi

from users.serializers import CartSerializer, FeaturedProductsSerializer

no_token = openapi.Response(
    description='no token provided',
    schema=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'error': openapi.Schema(type=openapi.TYPE_STRING)
        }
    )
)
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
        )
    ]
