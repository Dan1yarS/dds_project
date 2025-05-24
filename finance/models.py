# finance/models.py

from django.db import models
from django.utils import timezone


class Status(models.Model):
    """Модель для хранения статусов операций."""
    name = models.CharField(max_length=100, unique=True, verbose_name="Название статуса")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Статус"
        verbose_name_plural = "Статусы"


class Type(models.Model):
    """Модель для хранения типов операций."""
    name = models.CharField(max_length=100, unique=True, verbose_name="Название типа")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Тип операции"
        verbose_name_plural = "Типы операций"


class Category(models.Model):
    """Модель для категорий, привязанных к определенному типу."""
    name = models.CharField(max_length=100, verbose_name="Название категории")
    type = models.ForeignKey(Type, on_delete=models.PROTECT, related_name="categories", verbose_name="Тип операции")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        unique_together = ('name', 'type')


class Subcategory(models.Model):
    """Модель для подкатегорий, привязанных к категории."""
    name = models.CharField(max_length=100, verbose_name="Название подкатегории")
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name="subcategories", verbose_name="Категория")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Подкатегория"
        verbose_name_plural = "Подкатегории"
        unique_together = ('name', 'category')


class Transaction(models.Model):
    """Модель для хранения записи о движении денежных средств."""
    created_date = models.DateField(default=timezone.now, verbose_name="Дата создания")
    amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Сумма")
    comment = models.TextField(blank=True, null=True, verbose_name="Комментарий")

    status = models.ForeignKey(Status, on_delete=models.PROTECT, verbose_name="Статус")
    type = models.ForeignKey(Type, on_delete=models.PROTECT, verbose_name="Тип")
    category = models.ForeignKey(Category, on_delete=models.PROTECT, verbose_name="Категория")
    subcategory = models.ForeignKey(Subcategory, on_delete=models.PROTECT, verbose_name="Подкатегория")

    def __str__(self):
        return f"{self.created_date} - {self.type} - {self.amount} руб."

    class Meta:
        verbose_name = "Транзакция"
        verbose_name_plural = "Транзакции"
        ordering = ['-created_date']