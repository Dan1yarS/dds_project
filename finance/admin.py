# finance/admin.py

from django.contrib import admin
from .models import Status, Type, Category, Subcategory, Transaction

@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)

@admin.register(Type)
class TypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'type')
    list_filter = ('type',)
    search_fields = ('name',)
    list_select_related = ('type',)

@admin.register(Subcategory)
class SubcategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category')
    list_filter = ('category__type', 'category')
    search_fields = ('name',)
    list_select_related = ('category',)

@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('id', 'created_date', 'type', 'category', 'subcategory', 'amount', 'status')
    list_filter = ('created_date', 'status', 'type', 'category')
    search_fields = ('comment', 'amount')
    date_hierarchy = 'created_date'
    list_select_related = ('status', 'type', 'category', 'subcategory')
    fieldsets = (
        ('Основная информация', {
            'fields': ('type', 'category', 'subcategory', 'amount', 'status')
        }),
        ('Дополнительно', {
            'fields': ('created_date', 'comment')
        }),
    )