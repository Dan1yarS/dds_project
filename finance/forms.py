# finance/forms.py

from django import forms
from .models import Transaction, Category, Subcategory


class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ['created_date', 'type', 'category', 'subcategory', 'status', 'amount', 'comment']
        widgets = {
            'created_date': forms.DateInput(attrs={'type': 'date'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            current_class = field.widget.attrs.get('class', '')
            field.widget.attrs['class'] = f'{current_class} form-control'

        self.fields['category'].queryset = Category.objects.none()
        self.fields['subcategory'].queryset = Subcategory.objects.none()

        if 'type' in self.data:
            try:
                type_id = int(self.data.get('type'))
                self.fields['category'].queryset = Category.objects.filter(type_id=type_id).order_by('name')
            except (ValueError, TypeError):
                pass

        if 'category' in self.data:
            try:
                category_id = int(self.data.get('category'))
                self.fields['subcategory'].queryset = Subcategory.objects.filter(category_id=category_id).order_by(
                    'name')
            except (ValueError, TypeError):
                pass

        elif self.instance and self.instance.pk:
            if self.instance.type:
                self.fields['category'].queryset = Category.objects.filter(type=self.instance.type).order_by('name')
            if self.instance.category:
                self.fields['subcategory'].queryset = Subcategory.objects.filter(
                    category=self.instance.category).order_by('name')


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'type']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'form-control'})
        self.fields['type'].widget.attrs.update({'class': 'form-select'})


class SubcategoryForm(forms.ModelForm):
    class Meta:
        model = Subcategory
        fields = ['name', 'category']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'form-control'})
        self.fields['category'].widget.attrs.update({'class': 'form-select'})