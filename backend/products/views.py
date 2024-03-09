from rest_framework import permissions
from rest_framework.viewsets import ReadOnlyModelViewSet

from products.filters import CustomSearchFilter
from products.models import Product, Brand, ChangeablePrice, AdditionalFields
from products.serializers import ProductSerializer, BrandSerializer, ChangeablePriceSerializer, \
    AdditionalFieldsSerializer, ProductDetailSerializer


class ProductViewSet(ReadOnlyModelViewSet):
    queryset = Product.objects.all().order_by('id').prefetch_related('changeable_prices', 'additional_fields', 'images'
                                                                     ).select_related('brand', 'subcategory')
    permission_classes = [permissions.AllowAny]
    filter_backends = [CustomSearchFilter]

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return ProductDetailSerializer
        return ProductSerializer

    def get_queryset(self):
        if self.action == 'list':
            return Product.objects.all().order_by('id').prefetch_related('changeable_prices', 'images')
        return self.queryset


class ChangeablePriceViewSet(ReadOnlyModelViewSet):
    queryset = ChangeablePrice.objects.all()
    serializer_class = ChangeablePriceSerializer
    permission_classes = [permissions.AllowAny]


class AdditionalDataViewSet(ReadOnlyModelViewSet):
    queryset = AdditionalFields.objects.all()
    serializer_class = AdditionalFieldsSerializer
    permission_classes = [permissions.AllowAny]
