from rest_framework import permissions
from rest_framework.viewsets import ReadOnlyModelViewSet

from products.models import Product, Brand, ChangeablePrice, AdditionalFields
from products.serializers import ProductSerializer, BrandSerializer, ChangeablePriceSerializer, \
    AdditionalFieldsSerializer


class ProductViewSet(ReadOnlyModelViewSet):
    queryset = Product.objects.all().prefetch_related('changeable_prices', 'additional_fields', 'images').select_related('brand',
                                                                                                            'subcategory')
    serializer_class = ProductSerializer
    permission_classes = [permissions.AllowAny]


class ChangeablePriceViewSet(ReadOnlyModelViewSet):
    queryset = ChangeablePrice.objects.all()
    serializer_class = ChangeablePriceSerializer
    permission_classes = [permissions.AllowAny]


class TagsViewSet(ReadOnlyModelViewSet):
    queryset = AdditionalFields.objects.all()
    serializer_class = AdditionalFieldsSerializer
    permission_classes = [permissions.AllowAny]
