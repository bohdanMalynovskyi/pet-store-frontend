from django.db.models import F, Prefetch
from django_filters.rest_framework import DjangoFilterBackend
from drf_yasg.utils import swagger_auto_schema
from rest_framework import permissions, filters
from rest_framework.viewsets import ReadOnlyModelViewSet

from categories.models import ProductCategory, AnimalCategory, SubCategory
from categories.serializers import ProductCategoryHierarchySerializer, SubCategoryHierarchySerializer, \
    AnimalCategoryHierarchySerializer
from products.docs import ordering_param, has_discount_param, is_new_param
from products.filters import CustomSearchFilter, CustomPagination, ProductFilter
from products.logic import get_serialized_category
from products.models import Product, ChangeablePrice, AdditionalFields, ProductImages
from products.serializers import ProductSerializer, ChangeablePriceSerializer, \
    AdditionalFieldsSerializer, ProductDetailSerializer


class ProductViewSet(ReadOnlyModelViewSet):
    queryset = Product.objects.all().select_related('subcategory', 'subcategory__product_category',
                                                    'subcategory__product_category__animal_category',
                                                    'brand').annotate(
        discount_price=F('price') - (F('price') * F('discount') / 100)).order_by('id')
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
                discount_price=F('price') - (F('price') * F('discount') / 100)).order_by('id')
        return queryset

    def get_ordering(self):
        ordering = self.request.query_params.get('ordering', None)
        if ordering:
            if ordering == 'price':
                return ['discount_price']
            elif ordering == '-price':
                return ['-discount_price']
        return super().get_ordering()

    @swagger_auto_schema(manual_parameters=[ordering_param, is_new_param, has_discount_param])
    def list(self, request, *args, **kwargs):
        """ Adds categories hierarchy on filtering"""
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        serializer = self.get_serializer(page, many=True)
        data = serializer.data

        if 'animal_category' in request.query_params or 'product_category' in request.query_params or 'subcategory' in request.query_params:
            try:
                categories = {}

                if subcategory_key := request.query_params.get("subcategory"):
                    subcategory = SubCategory.objects.filter(key=subcategory_key).first()
                    if subcategory:
                        categories['subcategory'] = get_serialized_category(SubCategory, subcategory_key,
                                                                            SubCategoryHierarchySerializer)
                        categories['product_category'] = get_serialized_category(ProductCategory,
                                                                                 subcategory.product_category.key,
                                                                                 ProductCategoryHierarchySerializer)
                        categories.update(get_serialized_category(AnimalCategory,
                                                                  subcategory.product_category.animal_category.key,
                                                                  AnimalCategoryHierarchySerializer) or {})

                elif product_category_key := request.query_params.get("product_category"):
                    product_category = ProductCategory.objects.filter(key=product_category_key).first()
                    if product_category:
                        categories['product_category'] = get_serialized_category(ProductCategory,
                                                                                 product_category_key,
                                                                                 ProductCategoryHierarchySerializer)
                        categories.update(
                            get_serialized_category(AnimalCategory, product_category.animal_category.key,
                                                    AnimalCategoryHierarchySerializer) or {})

                elif animal_category_key := request.query_params.get("animal_category"):
                    categories.update(get_serialized_category(AnimalCategory, animal_category_key,
                                                              AnimalCategoryHierarchySerializer) or {})

            except AttributeError:
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
