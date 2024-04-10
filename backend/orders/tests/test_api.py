import json
import time

from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from rest_framework.authtoken.models import Token

from backend.settings import NP
from orders.models import Order
from products.models import Product
from users.models import UnregisteredUser, HashCode, User, Cart, CartItem


class OrderViewSetTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create(email='testuser@example.com')
        self.unregistered_user = UnregisteredUser.objects.create(hash_code=HashCode.objects.create())
        self.token = Token.objects.create(user=self.user).key
        self.order1 = Order.objects.create(user=self.user, status='in_process', payment_type='cash')
        self.order2 = Order.objects.create(unregistered_user=self.unregistered_user, status='waiting_for_payment',
                                           payment_type='online')

    def test_get_orders_authenticated(self):
        url = reverse('orders-list')
        headers = {'Authorization': f'Token {self.token}'}
        response = self.client.get(url, headers=headers)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['status'], 'in_process')

    def test_get_orders_unregistered(self):
        url = reverse('orders-list')
        headers = {'User': f'Token {self.unregistered_user.hash_code.key}'}
        response = self.client.get(url, headers=headers)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['status'], 'waiting_for_payment')


class CreateOrderTestCase(APITestCase):
    def setUp(self):
        self.unregistered_user = UnregisteredUser.objects.create(first_name='Іван', last_name='Іванов',
                                                                 phone_number='0676542345',
                                                                 hash_code=HashCode.objects.create())
        self.product1 = Product.objects.get(id=1)
        self.cart1 = Cart.objects.create(unregistered_user=self.unregistered_user)
        self.cart_item1 = CartItem.objects.create(product=self.product1, cart=self.cart1, quantity=2)

    def test_create_order(self):
        url = reverse('create_order')
        data = {
            "payment_type": "cash",
            "warehouse_index": "55/145",
            "city_ref": "db5c88d0-391c-11dd-90d9-001a92567626"
        }
        headers = {'Cart': f'Token {self.unregistered_user.hash_code.key}'}
        response = self.client.post(url, headers=headers, data=data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        time.sleep(15)  # need to let NOVA POST API save data

        res = NP.internet_document.delete(Order.objects.filter(unregistered_user=self.unregistered_user).last().ref)
        self.assertEqual(res['success'], True)

    def test_create_order_empty_cart(self):
        self.cart_item1.delete()
        url = reverse('create_order')
        data = {
            "payment_type": "cash",
            "warehouse_index": "55/145",
            "city_ref": "db5c88d0-391c-11dd-90d9-001a92567626"
        }
        headers = {'User': f'Token {self.unregistered_user.hash_code.key}'}
        response = self.client.post(url, headers=headers, data=data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
