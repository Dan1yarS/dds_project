# finance/views.py
from django.contrib import messages
from django.db.models import ProtectedError
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from .models import Transaction, Status, Type, Category, Subcategory
from .forms import TransactionForm, CategoryForm, SubcategoryForm
from .filters import TransactionFilter


def transaction_list(request):
    base_queryset = Transaction.objects.select_related(
        'status', 'type', 'category', 'subcategory'
    ).all()
    transaction_filter = TransactionFilter(request.GET, queryset=base_queryset)
    context = {
        'filter': transaction_filter,
    }
    return render(request, 'finance/transaction_list.html', context)


def transaction_create(request):
    if request.method == 'POST':
        form = TransactionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('finance:transaction_list')
    else:
        form = TransactionForm()

    return render(request, 'finance/transaction_form.html', {'form': form, 'title': 'Создание транзакции'})


def transaction_update(request, pk):
    transaction = get_object_or_404(Transaction, pk=pk)
    if request.method == 'POST':
        form = TransactionForm(request.POST, instance=transaction)
        if form.is_valid():
            form.save()
            return redirect('finance:transaction_list')
    else:
        form = TransactionForm(instance=transaction)

    return render(request, 'finance/transaction_form.html', {'form': form, 'title': 'Редактирование транзакции'})


def transaction_delete(request, pk):
    transaction = get_object_or_404(Transaction, pk=pk)
    if request.method == 'POST':
        transaction.delete()
        return redirect('finance:transaction_list')
    return render(request, 'finance/transaction_confirm_delete.html', {'transaction': transaction})


# API-like views for dependent dropdowns
def load_categories(request):
    type_id = request.GET.get('type_id')
    categories = Category.objects.filter(type_id=type_id).order_by('name')
    return JsonResponse(list(categories.values('id', 'name')), safe=False)


def load_subcategories(request):
    category_id = request.GET.get('category_id')
    subcategories = Subcategory.objects.filter(category_id=category_id).order_by('name')
    return JsonResponse(list(subcategories.values('id', 'name')), safe=False)


# --- Dictionary (Lookup Tables) Management ---

def manage_dictionaries(request):
    return render(request, 'finance/manage_dictionaries.html')


class DictionaryContextMixin:
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        model_meta = self.model._meta
        context['title'] = model_meta.verbose_name_plural.capitalize()
        context['model_name_plural'] = model_meta.verbose_name_plural
        context['model_name_singular'] = model_meta.model_name
        context['add_url'] = reverse_lazy(f'finance:{model_meta.model_name}-create')
        return context


class StatusListView(DictionaryContextMixin, ListView):
    model = Status
    template_name = 'finance/dictionary_list.html'


class StatusCreateView(DictionaryContextMixin, CreateView):
    model = Status
    fields = ['name']
    template_name = 'finance/dictionary_form.html'
    success_url = reverse_lazy('finance:status-list')


class StatusUpdateView(DictionaryContextMixin, UpdateView):
    model = Status
    fields = ['name']
    template_name = 'finance/dictionary_form.html'
    success_url = reverse_lazy('finance:status-list')


class StatusDeleteView(DictionaryContextMixin, DeleteView):
    model = Status
    template_name = 'finance/dictionary_confirm_delete.html'
    success_url = reverse_lazy('finance:status-list')

    def post(self, request, *args, **kwargs):
        try:
            return super().delete(request, *args, **kwargs)
        except ProtectedError:
            messages.error(request, "Этот статус не может быть удален, так как он используется в транзакциях.")
            return redirect('finance:status-list')


class TypeListView(DictionaryContextMixin, ListView):
    model = Type
    template_name = 'finance/dictionary_list.html'


class TypeCreateView(DictionaryContextMixin, CreateView):
    model = Type
    fields = ['name']
    template_name = 'finance/dictionary_form.html'
    success_url = reverse_lazy('finance:type-list')


class TypeUpdateView(DictionaryContextMixin, UpdateView):
    model = Type
    fields = ['name']
    template_name = 'finance/dictionary_form.html'
    success_url = reverse_lazy('finance:type-list')


class TypeDeleteView(DictionaryContextMixin, DeleteView):
    model = Type
    template_name = 'finance/dictionary_confirm_delete.html'
    success_url = reverse_lazy('finance:type-list')


class CategoryListView(DictionaryContextMixin, ListView):
    model = Category
    template_name = 'finance/dictionary_list.html'


class CategoryCreateView(DictionaryContextMixin, CreateView):
    model = Category
    form_class = CategoryForm
    template_name = 'finance/dictionary_form.html'
    success_url = reverse_lazy('finance:category-list')


class CategoryUpdateView(DictionaryContextMixin, UpdateView):
    model = Category
    form_class = CategoryForm
    template_name = 'finance/dictionary_form.html'
    success_url = reverse_lazy('finance:category-list')


class CategoryDeleteView(DictionaryContextMixin, DeleteView):
    model = Category
    template_name = 'finance/dictionary_confirm_delete.html'
    success_url = reverse_lazy('finance:category-list')


class SubcategoryListView(DictionaryContextMixin, ListView):
    model = Subcategory
    template_name = 'finance/dictionary_list.html'


class SubcategoryCreateView(DictionaryContextMixin, CreateView):
    model = Subcategory
    form_class = SubcategoryForm
    template_name = 'finance/dictionary_form.html'
    success_url = reverse_lazy('finance:subcategory-list')


class SubcategoryUpdateView(DictionaryContextMixin, UpdateView):
    model = Subcategory
    form_class = SubcategoryForm
    template_name = 'finance/dictionary_form.html'
    success_url = reverse_lazy('finance:subcategory-list')


class SubcategoryDeleteView(DictionaryContextMixin, DeleteView):
    model = Subcategory
    template_name = 'finance/dictionary_confirm_delete.html'
    success_url = reverse_lazy('finance:subcategory-list')