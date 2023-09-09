import django_filters
from .models import Policy


class PolicyDateFilter(django_filters.FilterSet):
    created_date = django_filters.DateFromToRangeFilter(field_name='created_date')

    class Meta:
        model = Policy
        fields = []
