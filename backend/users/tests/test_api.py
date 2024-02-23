from django.urls import reverse
from rest_framework import status

from products.models import Product
from products.tests.test_api import ProductTestCase
from users.models import Cart, CartItem, FeaturedProducts, FeaturedItem
from users.serializers import CartSerializer, CartItemSerializer, FeaturedProductsSerializer, FeaturedItemSerializer
from rest_framework.test import APITestCase


class CartTestCase(APITestCase):
    def test_create_cart(self):
        url = reverse('create-cart')
        response = self.client.post(url)

        serializer = CartSerializer(Cart.objects.last())
        self.assertEqual(status.HTTP_201_CREATED, response.status_code)
        self.assertEqual(serializer.data, response.data)

    def setUp(self):
        super().setUp()
        self.product1 = Product.objects.get(id=1)
        self.product2 = Product.objects.get(id=2)
        self.cart = Cart.objects.create()
        self.cart_item1 = CartItem.objects.create(product=self.product1, cart=self.cart, quantity=2)

    def test_get_cart(self):
        url = reverse('get-cart', args=[self.cart.id])
        headers = {'Authorization': f'Token {self.cart.hash_code}'}
        response = self.client.get(url, headers=headers)

        serializer = CartSerializer(self.cart)

        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer.data, response.data)

    def test_add_to_cart(self):
        url = reverse('add-to-cart', args=[self.cart.id, self.product2.id])
        headers = {'Authorization': f'Token {self.cart.hash_code}'}
        self.client.post(url, headers=headers)

        self.assertEqual(self.cart.cart_items.last().quantity, 1)

        response = self.client.post(url, headers=headers)

        serializer = CartSerializer(self.cart)
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer.data, response.data)
        self.assertEqual(self.cart.cart_items.last().quantity, 2)

    def test_decrease_cart_item(self):
        url = reverse('decrease-quantity', args=[self.cart.id, self.product1.id])
        headers = {'Authorization': f'Token {self.cart.hash_code}'}
        self.client.post(url, headers=headers)

        self.cart.refresh_from_db()
        self.assertEqual(self.cart.cart_items.last().quantity, 1)

        response = self.client.post(url, headers=headers)

        serializer = CartSerializer(self.cart)

        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer.data, response.data)
        self.assertEqual(self.cart.cart_items.count(), 0)

    def test_delete_cart_item(self):
        url = reverse('delete-cart-item', args=[self.cart.id, self.product1.id])
        headers = {'Authorization': f'Token {self.cart.hash_code}'}
        response = self.client.post(url, headers=headers)

        serializer = CartSerializer(self.cart)

        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer.data, response.data)
        self.assertEqual(self.cart.cart_items.count(), 0)

    def test_clear_cart(self):
        url = reverse('clear-cart', args=[self.cart.id])
        headers = {'Authorization': f'Token {self.cart.hash_code}'}
        response = self.client.post(url, headers=headers)

        serializer = CartSerializer(self.cart)

        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer.data, response.data)
        self.assertEqual(self.cart.cart_items.count(), 0)


class FeaturedTestCase(APITestCase):
    def test_create_featured(self):
        url = reverse('create-featured')
        response = self.client.post(url)

        serializer = FeaturedProductsSerializer(FeaturedProducts.objects.last())
        self.assertEqual(status.HTTP_201_CREATED, response.status_code)
        self.assertEqual(serializer.data, response.data)

    def setUp(self):
        super().setUp()
        self.product1 = Product.objects.get(id=1)
        self.product2 = Product.objects.get(id=2)
        self.featured = FeaturedProducts.objects.create()
        self.featured_item1 = FeaturedItem.objects.create(product=self.product1, featured_products=self.featured)

    def test_get_featured(self):
        url = reverse('get-featured', args=[self.featured.id])
        headers = {'Authorization': f'Token {self.featured.hash_code}'}
        response = self.client.get(url, headers=headers)

        serializer = FeaturedProductsSerializer(self.featured)

        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer.data, response.data)

    def test_add_to_featured(self):
        url = reverse('add-to-featured', args=[self.featured.id, self.product2.id])
        headers = {'Authorization': f'Token {self.featured.hash_code}'}
        response = self.client.post(url, headers=headers)

        serializer = FeaturedProductsSerializer(self.featured)

        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer.data, response.data)

    def test_delete_cart_item(self):
        url = reverse('delete-featured-item', args=[self.featured.id, self.product1.id])
        headers = {'Authorization': f'Token {self.featured.hash_code}'}
        response = self.client.post(url, headers=headers)

        serializer = FeaturedProductsSerializer(self.featured)

        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer.data, response.data)

    def test_clear_cart(self):
        url = reverse('clear-featured', args=[self.featured.id])
        headers = {'Authorization': f'Token {self.featured.hash_code}'}
        response = self.client.post(url, headers=headers)

        serializer = FeaturedProductsSerializer(self.featured)

        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer.data, response.data)
