from drf_yasg import openapi

ordering_param = openapi.Parameter(
    name="ordering",
    in_=openapi.IN_QUERY,
    description="Sort products by price. Use `price` for ascending order or `-price` for descending order.",
    required=False,
    type=openapi.TYPE_STRING,
    enum=["price", "-price"]
)

is_new_param = openapi.Parameter(
    name="is_new",
    in_=openapi.IN_QUERY,
    description="Filter by new products. Use `true` to show only new products and `false` for others.",
    required=False,
    type=openapi.TYPE_BOOLEAN
)

has_discount_param = openapi.Parameter(
    name="has_discount",
    in_=openapi.IN_QUERY,
    description="Filter by products with a discount. Use `true` to show only discounted products and `false` for others.",
    required=False,
    type=openapi.TYPE_BOOLEAN
)
