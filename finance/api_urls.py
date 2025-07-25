# finance/api_urls.py

from django.urls import path, include
import rest_framework.routers
from . import api_views

# Создаем роутер и регистрируем наши ViewSet'ы
router = rest_framework.routers.DefaultRouter()
router.register(r'statuses', api_views.StatusViewSet)
router.register(r'types', api_views.TypeViewSet)
router.register(r'categories', api_views.CategoryViewSet)
router.register(r'subcategories', api_views.SubcategoryViewSet)
router.register(r'transactions', api_views.TransactionViewSet)

# URL-адреса API определяются автоматически роутером.
urlpatterns = [
    path('', include(router.urls)),
]