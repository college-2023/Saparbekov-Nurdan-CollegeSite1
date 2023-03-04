from django_filters import rest_framework as filters
from .models import Item


class CharFilterInFilter(filters.BaseInFilter, filters.CharFilter):
    pass


class ItemFilter(filters.FilterSet):
    category = CharFilterInFilter(field_name='category__slug', lookup_expr='in')
    type = CharFilterInFilter(field_name='type__slug', lookup_expr='in')
    company = CharFilterInFilter(field_name='company__slug', lookup_expr='in')
    min_price = filters.NumberFilter(field_name='price', lookup_expr='gte')
    max_price = filters.NumberFilter(field_name='price', lookup_expr='lte')
    order_by_asc_price = filters.OrderingFilter(
        fields=('price',),
        label='Sort by ascending price'
    )

    class Meta:
        model = Item
        fields = 'category company type min_price max_price order_by_asc_price'.split()


