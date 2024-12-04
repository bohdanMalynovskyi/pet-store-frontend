from django_filters import rest_framework as rest_filter

from orders.models import Order


class OrderFilter(rest_filter.FilterSet):
    is_finished = rest_filter.BooleanFilter(method='filter_is_finished')
    is_cancelled = rest_filter.BooleanFilter(method='filter_is_cancelled')
    is_current = rest_filter.BooleanFilter(method='filter_is_current')

    class Meta:
        model = Order
        fields = ['is_finished', 'is_cancelled', 'is_current']

    def filter_is_finished(self, queryset, name, value):
        if value:
            return queryset.filter(status='received')
        return queryset

    def filter_is_cancelled(self, queryset, name, value):
        if value:
            return queryset.filter(status='cancelled')
        return queryset

    def filter_is_current(self, queryset, name, value):
        if value:
            return queryset.exclude(status__in=('cancelled', 'received', 'returned'))
        return queryset
