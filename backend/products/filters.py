from django.contrib.postgres.search import SearchVector, SearchQuery, SearchRank
from rest_framework import filters
from rest_framework.pagination import PageNumberPagination

from products.models import Product


class CustomSearchFilter(filters.SearchFilter):
    def filter_queryset(self, request, queryset, view):
        search_term = self.get_search_terms(request)

        if not search_term:
            return queryset

        language = 'ukrainian'

        search_vector = SearchVector('name', 'description', 'brand__name', 'subcategory__name',
                                     'additional_fields__text', config=language)
        search_query = SearchQuery(str(search_term), config=language)
        rank = SearchRank(search_vector, search_query)

        queryset = Product.objects.annotate(
            search=search_vector, rank=rank).filter(
            search=search_query).order_by('-rank')

        return queryset


class CustomPagination(PageNumberPagination):
    page_size = 10
