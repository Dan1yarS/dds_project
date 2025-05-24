# finance/urls.py

from django.urls import path
from . import views

app_name = 'finance'

urlpatterns = [
    path('', views.transaction_list, name='transaction_list'),
    path('transaction/add/', views.transaction_create, name='transaction_create'),
    path('transaction/<int:pk>/edit/', views.transaction_update, name='transaction_update'),
    path('transaction/<int:pk>/delete/', views.transaction_delete, name='transaction_delete'),

    path('ajax/load-categories/', views.load_categories, name='ajax_load_categories'),
    path('ajax/load-subcategories/', views.load_subcategories, name='ajax_load_subcategories'),

    path('manage/', views.manage_dictionaries, name='manage_dictionaries'),

    path('manage/statuses/', views.StatusListView.as_view(), name='status-list'),
    path('manage/statuses/add/', views.StatusCreateView.as_view(), name='status-create'),
    path('manage/statuses/<int:pk>/edit/', views.StatusUpdateView.as_view(), name='status-update'),
    path('manage/statuses/<int:pk>/delete/', views.StatusDeleteView.as_view(), name='status-delete'),

    path('manage/types/', views.TypeListView.as_view(), name='type-list'),
    path('manage/types/add/', views.TypeCreateView.as_view(), name='type-create'),
    path('manage/types/<int:pk>/edit/', views.TypeUpdateView.as_view(), name='type-update'),
    path('manage/types/<int:pk>/delete/', views.TypeDeleteView.as_view(), name='type-delete'),

    path('manage/categories/', views.CategoryListView.as_view(), name='category-list'),
    path('manage/categories/add/', views.CategoryCreateView.as_view(), name='category-create'),
    path('manage/categories/<int:pk>/edit/', views.CategoryUpdateView.as_view(), name='category-update'),
    path('manage/categories/<int:pk>/delete/', views.CategoryDeleteView.as_view(), name='category-delete'),

    path('manage/subcategories/', views.SubcategoryListView.as_view(), name='subcategory-list'),
    path('manage/subcategories/add/', views.SubcategoryCreateView.as_view(), name='subcategory-create'),
    path('manage/subcategories/<int:pk>/edit/', views.SubcategoryUpdateView.as_view(), name='subcategory-update'),
    path('manage/subcategories/<int:pk>/delete/', views.SubcategoryDeleteView.as_view(), name='subcategory-delete'),
]