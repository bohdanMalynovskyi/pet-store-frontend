from rest_framework import serializers

from categories.models import AnimalCategory, ProductCategory, SubCategory


class SubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SubCategory
        fields = ['id', 'key', 'name']


class ProductCategorySerializer(serializers.ModelSerializer):
    subcategories = SubCategorySerializer(many=True, read_only=True)

    class Meta:
        model = ProductCategory
        fields = ['id', 'key', 'name', 'subcategories']


class AnimalCategorySerializer(serializers.ModelSerializer):
    product_categories = ProductCategorySerializer(many=True, read_only=True)

    class Meta:
        model = AnimalCategory
        fields = ['id', 'key', 'name', 'product_categories']


class SubCategoryHierarchySerializer(serializers.ModelSerializer):
    class Meta:
        model = SubCategory
        fields = ['id', 'key', 'name']


class ProductCategoryHierarchySerializer(serializers.ModelSerializer):
    subcategory = SubCategoryHierarchySerializer(read_only=True)

    class Meta:
        model = ProductCategory
        fields = ['id', 'key', 'name', 'subcategory']


class AnimalCategoryHierarchySerializer(serializers.ModelSerializer):
    product_category = ProductCategoryHierarchySerializer(read_only=True)

    class Meta:
        model = AnimalCategory
        fields = ['id', 'key', 'name', 'product_category']
