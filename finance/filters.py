# finance/filters.py

import django_filters
from django import forms

from .models import Transaction


class TransactionFilter(django_filters.FilterSet):
    start_date = django_filters.DateFilter(
        field_name='created_date',
        lookup_expr='gte',
        label='Дата, от',
        widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'})
    )
    end_date = django_filters.DateFilter(
        field_name='created_date',
        lookup_expr='lte',
        label='Дата, до',
        widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'})
    )

    class Meta:
        model = Transaction
        fields = ['status', 'type', 'category', 'subcategory']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Добавляем классы ко всем полям-селектам
        for field_name, field in self.form.fields.items():
            if isinstance(field, forms.ModelChoiceField):
                field.widget.attrs.update({'class': 'form-select'})
