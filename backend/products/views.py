from django.db.models import F
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import permissions, filters
from rest_framework.viewsets import ReadOnlyModelViewSet

from categories.serializers import ProductCategoryHierarchySerializer, SubCategoryHierarchySerializer, \
    AnimalCategoryHierarchySerializer, ProductCategorySerializer, SubCategorySerializer, AnimalCategorySerializer
from products.filters import CustomSearchFilter, CustomPagination
from products.models import Product, ChangeablePrice, AdditionalFields
from products.serializers import ProductSerializer, ChangeablePriceSerializer, \
    AdditionalFieldsSerializer, ProductDetailSerializer


class ProductViewSet(ReadOnlyModelViewSet):
    queryset = Product.objects.all().prefetch_related('changeable_prices', 'additional_fields',
                                                      'images').select_related('brand', 'subcategory')
    permission_classes = [permissions.AllowAny]
    filter_backends = [CustomSearchFilter, filters.OrderingFilter]
    ordering_fields = ('price',)
    pagination_class = CustomPagination

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return ProductDetailSerializer
        return ProductSerializer

    def get_queryset(self):
        """ Handles filtering """
        queryset = super().get_queryset()
        if self.action == 'list':
            queryset = Product.objects.all().prefetch_related('changeable_prices', 'images').annotate(
                discount_price=F('price') - (F('price') * F('discount') / 100))

            min_price = self.request.query_params.get('min_price')
            max_price = self.request.query_params.get('max_price')
            subcategory = self.request.query_params.get('subcategory')
            animal_category = self.request.query_params.get('animal_category')
            product_category = self.request.query_params.get('product_category')
            has_discount = self.request.query_params.get('has_discount')

            if min_price is not None:
                queryset = queryset.filter(discount_price__gte=min_price)

            if max_price is not None:
                queryset = queryset.filter(discount_price__lte=max_price)

            if subcategory is not None:
                queryset = queryset.filter(subcategory_id=subcategory)

            if animal_category is not None:
                queryset = queryset.filter(subcategory__product_category__animal_category_id=animal_category)

            if product_category is not None:
                queryset = queryset.filter(subcategory__product_category_id=product_category)

            if has_discount is not None:
                queryset = queryset.filter(discount__gt=0) if has_discount.lower() == 'true' else queryset.filter(
                    discount=0)

        return queryset

    def get_ordering(self):
        ordering = self.request.query_params.get('ordering', None)
        if ordering:
            if ordering == 'price':
                return ['discount_price']
            elif ordering == '-discount_price':
                return ['-price']
        return super().get_ordering()

    @swagger_auto_schema(manual_parameters=[
        openapi.Parameter('min_price', openapi.IN_QUERY, description="Minimum price filter", type=openapi.TYPE_NUMBER),
        openapi.Parameter('max_price', openapi.IN_QUERY, description="Maximum price filter", type=openapi.TYPE_NUMBER),
        openapi.Parameter('subcategory', openapi.IN_QUERY, description="Subcategory filter", type=openapi.TYPE_INTEGER),
        openapi.Parameter('animal_category', openapi.IN_QUERY, description="Animal category filter",
                          type=openapi.TYPE_INTEGER),
        openapi.Parameter('product_category', openapi.IN_QUERY, description="Product category filter",
                          type=openapi.TYPE_INTEGER),
        openapi.Parameter('has_discount', openapi.IN_QUERY, description="Does have discount",
                          type=openapi.TYPE_BOOLEAN),
        openapi.Parameter('ordering', openapi.IN_QUERY,
                          description="value 'price' order data ascending and value '-price' descending",
                          type=openapi.TYPE_INTEGER),
    ])
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
