from django.test import TestCase

from categories.models import SubCategory, AnimalCategory, ProductCategory
from categories.serializers import AnimalCategorySerializer, ProductCategorySerializer, SubCategorySerializer, \
    AnimalCategoryHierarchySerializer, ProductCategoryHierarchySerializer, SubCategoryHierarchySerializer


class AnimalCategoryTests(TestCase):
    fixtures = ['base_data.json']

    def setUp(self):
        self.animal_category = AnimalCategory.objects.create(name='Dog', key='dog')

    def test_ok(self):
        expected_data = {
            'id': self.animal_category.id,
            'key': 'dog',
            'name': 'Dog',
            'product_categories': []
        }
        data = AnimalCategorySerializer(self.animal_category).data
        self.assertEqual(expected_data, data)


class ProductCategoryTests(AnimalCategoryTests):

    def setUp(self):
        super().setUp()
        self.product_category = ProductCategory.objects.create(name='Food', animal_category=self.animal_category)

    def test_ok(self):
        expected_data = {
            'id': self.product_category.id,
            'key': '',
            'name': 'Food',
            'subcategories': []
        }
        data = ProductCategorySerializer(self.product_category).data
        self.assertEqual(expected_data, data)


class SubCategoryTests(ProductCategoryTests):
    def setUp(self):
        super().setUp()
        self.sub_category = SubCategory.objects.create(name='Wet food', product_category=self.product_category)

    def test_ok(self):
        expected_data = {
            'id': self.sub_category.id,
            'key': '',
            'name': 'Wet food'
        }
        data = SubCategorySerializer(self.sub_category).data
        self.assertEqual(expected_data, data)


class AnimalCategoryHierarchyTests(TestCase):
    fixtures = ['base_data.json']

    def setUp(self):
        self.animal_category = AnimalCategory.objects.create(name='Dog', key='dog')

    def test_ok(self):
        expected_data = {
            'id': self.animal_category.id,
            'key': 'dog',
            'name': 'Dog',
        }
        data = AnimalCategoryHierarchySerializer(self.animal_category).data
        self.assertEqual(expected_data, data)


class ProductCategoryHierarchyTests(AnimalCategoryHierarchyTests):

    def setUp(self):
        super().setUp()
        self.product_category = ProductCategory.objects.create(name='Food', animal_category=self.animal_category)

    def test_ok(self):
        expected_data = {
            'id': self.product_category.id,
            'key': '',
            'name': 'Food',
        }
        data = ProductCategoryHierarchySerializer(self.product_category).data
        self.assertEqual(expected_data, data)


class SubCategoryHierarchyTests(ProductCategoryHierarchyTests):
    def setUp(self):
        super().setUp()
        self.sub_category = SubCategory.objects.create(name='Wet food', product_category=self.product_category)

    def test_ok(self):
        expected_data = {
            'id': self.sub_category.id,
            'key': '',
            'name': 'Wet food'
        }
        data = SubCategoryHierarchySerializer(self.sub_category).data
        self.assertEqual(expected_data, data)
