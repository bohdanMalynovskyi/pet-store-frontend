from django.db.models import F
from rest_framework import permissions, filters
from rest_framework.viewsets import ReadOnlyModelViewSet

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
        if self.action == 'list':
            queryset = Product.objects.all().prefetch_related('changeable_prices', 'images').annotate(
                discount_price=F('price') - (F('price') * F('discount') / 100))

            min_price = self.request.query_params.get('min_price')
            max_price = self.request.query_params.get('max_price')
            subcategory = self.request.query_params.get('subcategory')
            animal_category = self.request.query_params.get('animal_category')
            product_category = self.request.query_params.get('product_category')

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

            return queryset
        else:
            return self.queryset

    def get_ordering(self):
        ordering = self.request.query_params.get('ordering', None)
        if ordering:
            if ordering == 'price':
                return ['discount_price']
            elif ordering == '-discount_price':
                return ['-price']
        return super().get_ordering()


class ChangeablePriceViewSet(ReadOnlyModelViewSet):
    queryset = ChangeablePrice.objects.all()
    serializer_class = ChangeablePriceSerializer
    permission_classes = [permissions.AllowAny]


class AdditionalDataViewSet(ReadOnlyModelViewSet):
    queryset = AdditionalFields.objects.all()
    serializer_class = AdditionalFieldsSerializer
    permission_classes = [permissions.AllowAny]
