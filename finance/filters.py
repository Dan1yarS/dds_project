# finance/filters.py

import django_filters
from .models import Transaction

class TransactionFilter(django_filters.FilterSet):
    start_date = django_filters.DateFilter(
        field_name='created_date',
        lookup_expr='gte',
        label='Дата, от'
    )
    end_date = django_filters.DateFilter(
        field_name='created_date',
        lookup_expr='lte',
        label='Дата, до'
    )

    class Meta:
        model = Transaction
        fields = ['status', 'type', 'category', 'subcategory']