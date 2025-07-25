# finance/serializers.py

from rest_framework import serializers
from .models import Status, Type, Category, Subcategory, Transaction


class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = ['id', 'name']


class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type
        fields = ['id', 'name']


class SubcategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Subcategory
        fields = ['id', 'name', 'category']


class CategorySerializer(serializers.ModelSerializer):
    # Отображаем связанные подкатегории только для чтения
    subcategories = SubcategorySerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ['id', 'name', 'type', 'subcategories']


class TransactionSerializer(serializers.ModelSerializer):
    # Используем строковые представления для связанных полей для удобства
    status = serializers.StringRelatedField()
    type = serializers.StringRelatedField()
    category = serializers.StringRelatedField()
    subcategory = serializers.StringRelatedField()

    class Meta:
        model = Transaction
        fields = [
            'id',
            'created_date',
            'status',
            'type',
            'category',
            'subcategory',
            'amount',
            'comment'
        ]

    # Добавляем валидацию, чтобы категория соответствовала типу
    def validate(self, data):
        category = data.get('category')
        type_obj = data.get('type')

        if category and type_obj and category.type != type_obj:
            raise serializers.ValidationError("Выбранная категория не относится к указанному типу.")

        # Аналогичная проверка для подкатегории и категории
        subcategory = data.get('subcategory')
        if subcategory and category and subcategory.category != category:
            raise serializers.ValidationError("Выбранная подкатегория не относится к указанной категории.")

        return data
