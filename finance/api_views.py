# finance/api_views.py

from rest_framework import viewsets, permissions
from .models import Status, Type, Category, Subcategory, Transaction
from .serializers import (
    StatusSerializer, TypeSerializer, CategorySerializer,
    SubcategorySerializer, TransactionSerializer
)
from .filters import TransactionFilter
from django_filters.rest_framework import DjangoFilterBackend


class StatusViewSet(viewsets.ModelViewSet):
    """ API-эндпоинт для управления статусами. """
    queryset = Status.objects.all()
    serializer_class = StatusSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]  # Пример разрешений


class TypeViewSet(viewsets.ModelViewSet):
    """ API-эндпоинт для управления типами. """
    queryset = Type.objects.all()
    serializer_class = TypeSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class CategoryViewSet(viewsets.ModelViewSet):
    """ API-эндпоинт для управления категориями. """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class SubcategoryViewSet(viewsets.ModelViewSet):
    """ API-эндпоинт для управления подкатегориями. """
    queryset = Subcategory.objects.all()
    serializer_class = SubcategorySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class TransactionViewSet(viewsets.ModelViewSet):
    """ API-эндпоинт для просмотра и редактирования транзакций. """
    queryset = Transaction.objects.select_related(
        'status', 'type', 'category', 'subcategory'
    ).all()
    serializer_class = TransactionSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    # Подключаем фильтрацию из вашего файла filters.py
    filter_backends = [DjangoFilterBackend]
    filterset_class = TransactionFilter
