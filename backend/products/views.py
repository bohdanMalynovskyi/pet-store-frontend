from rest_framework import permissions
from rest_framework.viewsets import ReadOnlyModelViewSet

from products.models import Product, Brand, ChangeablePrice, Tags
from products.serializers import ProductSerializer, BrandSerializer, ChangeablePriceSerializer, TagsSerializer


class ProductViewSet(ReadOnlyModelViewSet):
    queryset = Product.objects.all().prefetch_related('changeable_prices', 'tags', 'images').select_related('brand',
                                                                                                            'subcategory')
    serializer_class = ProductSerializer
    permission_classes = [permissions.AllowAny]


class ChangeablePriceViewSet(ReadOnlyModelViewSet):
    queryset = ChangeablePrice.objects.all()
    serializer_class = ChangeablePriceSerializer
    permission_classes = [permissions.AllowAny]


class TagsViewSet(ReadOnlyModelViewSet):
    queryset = Tags.objects.all()
    serializer_class = TagsSerializer
    permission_classes = [permissions.AllowAny]

