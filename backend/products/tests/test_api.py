from django.test import TestCase
from django.urls import reverse
from rest_framework import status

from categories.models import AnimalCategory, ProductCategory, SubCategory
from categories.serializers import AnimalCategorySerializer, ProductCategorySerializer, SubCategorySerializer
from rest_framework.test import APITestCase

from categories.tests.test_api import SubCategoryTestCase
from products.models import Brand, Product, ChangeablePrice, Tags
from products.serializers import ProductSerializer, ChangeablePriceSerializer, TagsSerializer


class ProductTestCase(SubCategoryTestCase):
    def setUp(self):
        super().setUp()
        self.brand = Brand.objects.create(name='Purina', country='United States')
        self.product = Product.objects.create(name='ProPlan', subcategory=self.subcategory1, sale=50, price=100,
                                              description='cool', brand=self.brand)

    def test_get_list(self):
        url = reverse('products-list')
        products = Product.objects.all()
        response = self.client.get(url)
        serializer_data = ProductSerializer(products, many=True).data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.data)

    def test_get_detail(self):
        url = reverse('products-detail', args=(self.product.id,))
        response = self.client.get(url)
        serializer_data = ProductSerializer(self.product, ).data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.data)

    def test_get_detail_not_found(self):
        url = reverse('products-detail', args=(122,))
        response = self.client.get(url)
        self.assertEqual(status.HTTP_404_NOT_FOUND, response.status_code)
        self.assertEqual({"detail": "Not found."}, response.data)

    def test_post_detail_not_allowed(self):
        url = reverse('products-list')
        response = self.client.post(url)
        self.assertEqual(status.HTTP_405_METHOD_NOT_ALLOWED, response.status_code)
        self.assertEqual({"detail": "Method \"POST\" not allowed."}, response.data)


class ChangeablePriceTestCase(ProductTestCase):
    def setUp(self):
        super().setUp()
        self.changeable_price = ChangeablePrice.objects.create(price=100, sale=50, product=self.product, order=1,
                                                               size='S')

    def test_get_list(self):
        url = reverse('changeableprices-list')
        changeable_prices = ChangeablePrice.objects.all()
        response = self.client.get(url)
        serializer_data = ChangeablePriceSerializer(changeable_prices, many=True).data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.data)

    def test_get_detail(self):
        url = reverse('changeableprices-detail', args=(self.changeable_price.id,))
        response = self.client.get(url)
        serializer_data = ChangeablePriceSerializer(self.changeable_price, ).data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.data)

    def test_get_detail_not_found(self):
        url = reverse('changeableprices-detail', args=(122,))
        response = self.client.get(url)
        self.assertEqual(status.HTTP_404_NOT_FOUND, response.status_code)
        self.assertEqual({"detail": "Not found."}, response.data)

    def test_post_detail_not_allowed(self):
        url = reverse('changeableprices-list')
        response = self.client.post(url)
        self.assertEqual(status.HTTP_405_METHOD_NOT_ALLOWED, response.status_code)
        self.assertEqual({"detail": "Method \"POST\" not allowed."}, response.data)


class TagsTestCase(ProductTestCase):
    def setUp(self):
        super().setUp()
        self.tag = Tags.objects.create(title='title', product=self.product, text='text')

    def test_get_list(self):
        url = reverse('tags-list')
        tags = Tags.objects.all()
        response = self.client.get(url)
        serializer_data = TagsSerializer(tags, many=True).data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.data)

    def test_get_detail(self):
        url = reverse('tags-detail', args=(self.tag.id,))
        response = self.client.get(url)
        serializer_data = TagsSerializer(self.tag, ).data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.data)

    def test_get_detail_not_found(self):
        url = reverse('tags-detail', args=(122,))
        response = self.client.get(url)
        self.assertEqual(status.HTTP_404_NOT_FOUND, response.status_code)
        self.assertEqual({"detail": "Not found."}, response.data)

    def test_post_detail_not_allowed(self):
        url = reverse('tags-list')
        response = self.client.post(url)
        self.assertEqual(status.HTTP_405_METHOD_NOT_ALLOWED, response.status_code)
        self.assertEqual({"detail": "Method \"POST\" not allowed."}, response.data)