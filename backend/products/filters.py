from django.contrib.postgres.search import SearchVector, SearchQuery, SearchRank
from rest_framework import filters
from rest_framework.pagination import PageNumberPagination

from products.models import Product

from django_filters import rest_framework as rest_filter


class CustomSearchFilter(filters.SearchFilter):
    def filter_queryset(self, request, queryset, view):
        search_term = self.get_search_terms(request)

        if not search_term:
            return queryset

        language = 'ukrainian'

        search_vector = SearchVector('name', 'description', 'brand__name', 'subcategory__name',
                                     'subcategory__product_category__animal_category__name',
                                     'subcategory__product_category__name',
                                     'additional_fields__text', config=language)
        search_query = SearchQuery(str(search_term), config=language, search_type='websearch')
        rank = SearchRank(search_vector, search_query)

        queryset = Product.objects.annotate(
            search=search_vector, rank=rank).filter(
            search=search_query).order_by('-rank')

        return queryset


class CustomPagination(PageNumberPagination):
    page_size = 10


class ProductFilter(rest_filter.FilterSet):
    min_price = rest_filter.NumberFilter(field_name="discount_price", lookup_expr='gte')
    max_price = rest_filter.NumberFilter(field_name="discount_price", lookup_expr='lte')
    subcategory = rest_filter.CharFilter(field_name="subcategory__key")
    animal_category = rest_filter.CharFilter(field_name="subcategory__product_category__animal_category__key")
    product_category = rest_filter.CharFilter(field_name="subcategory__product_category__key")
    has_discount = rest_filter.BooleanFilter(method='filter_has_discount')
    is_new = rest_filter.BooleanFilter(field_name="is_new")

    class Meta:
        model = Product
        fields = ['min_price', 'max_price', 'subcategory', 'animal_category', 'product_category', 'has_discount',
                  'is_new']

    def filter_has_discount(self, queryset, name, value):
        return queryset.filter(discount__gt=0) if value else queryset.filter(discount=0)
