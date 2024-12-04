from django.db.models import F, Prefetch
from django_filters.rest_framework import DjangoFilterBackend
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import permissions, filters
from rest_framework.viewsets import ReadOnlyModelViewSet

from categories.serializers import ProductCategoryHierarchySerializer, SubCategoryHierarchySerializer, \
    AnimalCategoryHierarchySerializer
from products.filters import CustomSearchFilter, CustomPagination, ProductFilter
from products.models import Product, ChangeablePrice, AdditionalFields, ProductImages
from products.serializers import ProductSerializer, ChangeablePriceSerializer, \
    AdditionalFieldsSerializer, ProductDetailSerializer


class ProductViewSet(ReadOnlyModelViewSet):
    queryset = Product.objects.all().select_related('subcategory', 'subcategory__product_category',
                                                    'subcategory__product_category__animal_category',
                                                    'brand').annotate(
        discount_price=F('price') - (F('price') * F('discount') / 100))
    permission_classes = [permissions.AllowAny]
    filter_backends = [DjangoFilterBackend, CustomSearchFilter, filters.OrderingFilter]
    ordering_fields = ('price',)
    pagination_class = CustomPagination
    filterset_class = ProductFilter

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return ProductDetailSerializer
        return ProductSerializer

    def get_queryset(self):
        """ Handles filtering """
        queryset = super().get_queryset()
        if self.action == 'list':
            queryset = Product.objects.all().prefetch_related('changeable_prices', Prefetch('images',
                                                                                            queryset=ProductImages.objects.filter(
                                                                                                order=1),
                                                                                            to_attr='filtered_images')).select_related(
                'subcategory', 'subcategory__product_category', 'subcategory__product_category__animal_category',
                'brand').annotate(
                discount_price=F('price') - (F('price') * F('discount') / 100))
        return queryset

    def get_ordering(self):
        ordering = self.request.query_params.get('ordering', None)
        if ordering:
            if ordering == 'price':
                return ['discount_price']
            elif ordering == '-discount_price':
                return ['-price']
        return super().get_ordering()

    def list(self, request, *args, **kwargs):
        """ Adds categories hierarchy on filtering"""
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        serializer = self.get_serializer(page, many=True)
        data = serializer.data

        if 'animal_category' in request.query_params or 'product_category' in request.query_params or 'subcategory' in request.query_params:
            try:
                item = page[0]
                animal_category = item.subcategory.product_category.animal_category
                serialized_category = AnimalCategoryHierarchySerializer(animal_category, many=False)
                categories = serialized_category.data

                if 'product_category' in request.query_params or 'subcategory' in request.query_params:
                    product_category = item.subcategory.product_category
                    serialized_category = ProductCategoryHierarchySerializer(product_category, many=False)
                    categories['product_category'] = serialized_category.data

                    if 'subcategory' in request.query_params:
                        subcategory = item.subcategory
                        serialized_category = SubCategoryHierarchySerializer(subcategory, many=False)
                        categories['subcategory'] = serialized_category.data
            except IndexError:
                categories = None

            response = self.get_paginated_response(data)
            response.data['categories'] = categories
        else:
            response = self.get_paginated_response(data)

        return response


class ChangeablePriceViewSet(ReadOnlyModelViewSet):
    queryset = ChangeablePrice.objects.all()
    serializer_class = ChangeablePriceSerializer
    permission_classes = [permissions.AllowAny]


class AdditionalDataViewSet(ReadOnlyModelViewSet):
    queryset = AdditionalFields.objects.all()
    serializer_class = AdditionalFieldsSerializer
    permission_classes = [permissions.AllowAny]
