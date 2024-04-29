from drf_yasg import openapi

create_order_body = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        'payment_type': openapi.Schema(type=openapi.TYPE_STRING, enum=["cash", "online"]),
        'warehouse_index': openapi.Schema(type=openapi.TYPE_STRING),
        'city_ref': openapi.Schema(type=openapi.TYPE_STRING),
        'first_name': openapi.Schema(type=openapi.TYPE_STRING, description='required if not authenticated'),
        'second_name': openapi.Schema(type=openapi.TYPE_STRING),
        'last_name': openapi.Schema(type=openapi.TYPE_STRING, description='required if not authenticated'),
        'phone': openapi.Schema(type=openapi.TYPE_STRING, description='required if not authenticated'),
    },
    required=['payment_type', 'warehouse_index', 'city_ref']
)

get_warehouse_body = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        'city_name': openapi.Schema(type=openapi.TYPE_STRING),
        'find_by_string': openapi.Schema(type=openapi.TYPE_STRING),
    },
    required=['city_name', 'find_by_string']
)
