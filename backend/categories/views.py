from rest_framework import viewsets, permissions

from categories.models import AnimalCategory, ProductCategory, SubCategory
from categories.serializers import AnimalCategorySerializer, ProductCategorySerializer, SubCategorySerializer


class AnimalCategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = AnimalCategory.objects.all().prefetch_related('product_categories', 'product_categories__subcategories')
    serializer_class = AnimalCategorySerializer
    permission_classes = [permissions.AllowAny]
    lookup_field = 'key'


class ProductCategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ProductCategory.objects.all().prefetch_related('subcategories')
    serializer_class = ProductCategorySerializer
    permission_classes = [permissions.AllowAny]
    lookup_field = 'key'


class SubCategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = SubCategory.objects.all()
    serializer_class = SubCategorySerializer
    permission_classes = [permissions.AllowAny]
    lookup_field = 'key'
