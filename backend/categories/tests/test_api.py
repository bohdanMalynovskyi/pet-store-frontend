from django.urls import reverse
from rest_framework import status

from categories.models import AnimalCategory, ProductCategory, SubCategory
from categories.serializers import AnimalCategorySerializer, ProductCategorySerializer, SubCategorySerializer
from rest_framework.test import APITestCase


class AnimalCategoryTestCase(APITestCase):
    fixtures = ['base_data.json']

    def setUp(self):
        self.animal_category1 = AnimalCategory.objects.create(name='Dog', key='dogss')
        self.animal_category2 = AnimalCategory.objects.create(name='Cat', key='catss')

    def test_get_list(self):
        url = reverse('animalcategory-list')
        categories = AnimalCategory.objects.all()
        response = self.client.get(url)
        serializer_data = AnimalCategorySerializer(categories, many=True).data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.data)

    def test_get_detail(self):
        url = reverse('animalcategory-detail', args=(self.animal_category1.key,))
        response = self.client.get(url)
        serializer_data = AnimalCategorySerializer(self.animal_category1, ).data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.data)

    def test_get_detail_not_found(self):
        url = reverse('animalcategory-detail', args=(122,))
        response = self.client.get(url)
        self.assertEqual(status.HTTP_404_NOT_FOUND, response.status_code)
        self.assertEqual({"detail": "Not found."}, response.data)

    def test_post_detail_not_allowed(self):
        url = reverse('animalcategory-list')
        response = self.client.post(url)
        self.assertEqual(status.HTTP_405_METHOD_NOT_ALLOWED, response.status_code)
        self.assertEqual({"detail": "Method \"POST\" not allowed."}, response.data)


class ProductCategoryTestCase(AnimalCategoryTestCase):
    def setUp(self):
        super().setUp()
        self.product_category1 = ProductCategory.objects.create(key='fooood', name='Food', animal_category=self.animal_category1)
        self.product_category2 = ProductCategory.objects.create(key='tooooy', name='Toy', animal_category=self.animal_category2)

    def test_get_list(self):
        url = reverse('productcategory-list')
        product_categories = ProductCategory.objects.all()
        response = self.client.get(url)
        serializer_data = ProductCategorySerializer(product_categories, many=True).data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.data)

    def test_get_detail(self):
        url = reverse('productcategory-detail', args=(self.product_category1.key,))
        response = self.client.get(url)
        serializer_data = ProductCategorySerializer(self.product_category1, ).data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.data)

    def test_get_detail_not_found(self):
        url = reverse('productcategory-detail', args=(122,))
        response = self.client.get(url)
        self.assertEqual(status.HTTP_404_NOT_FOUND, response.status_code)
        self.assertEqual({"detail": "Not found."}, response.data)

    def test_post_detail_not_allowed(self):
        url = reverse('productcategory-list')
        response = self.client.post(url)
        self.assertEqual(status.HTTP_405_METHOD_NOT_ALLOWED, response.status_code)
        self.assertEqual({"detail": "Method \"POST\" not allowed."}, response.data)


class SubCategoryTestCase(ProductCategoryTestCase):
    def setUp(self):
        super().setUp()
        self.subcategory1 = SubCategory.objects.create(key='weet_fooood', name='Wet food', product_category=self.product_category1)
        self.subcategory2 = SubCategory.objects.create(key='toooy_booone', name='Toy bone', product_category=self.product_category2)

    def test_get_list(self):
        url = reverse('subcategory-list')
        subcategories = SubCategory.objects.all()
        response = self.client.get(url)
        serializer_data = SubCategorySerializer(subcategories, many=True).data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.data)

    def test_get_detail(self):
        url = reverse('subcategory-detail', args=(self.subcategory1.key,))
        response = self.client.get(url)
        serializer_data = SubCategorySerializer(self.subcategory1, ).data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.data)

    def test_get_detail_not_found(self):
        url = reverse('subcategory-detail', args=(122,))
        response = self.client.get(url)
        self.assertEqual(status.HTTP_404_NOT_FOUND, response.status_code)
        self.assertEqual({"detail": "Not found."}, response.data)

    def test_post_detail_not_allowed(self):
        url = reverse('subcategory-list')
        response = self.client.post(url)
        self.assertEqual(status.HTTP_405_METHOD_NOT_ALLOWED, response.status_code)
        self.assertEqual({"detail": "Method \"POST\" not allowed."}, response.data)
