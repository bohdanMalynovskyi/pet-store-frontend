import time
from time import sleep

from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from rest_framework.authtoken.models import Token

from backend.settings import NP
from orders.models import Order
from products.models import Product
from users.models import HashCode, User, Cart, CartItem


class OrderViewSetTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create(email='testuser@example.com')
        self.token = Token.objects.create(user=self.user).key
        self.order1 = Order.objects.create(user=self.user, status='in_process', payment_type='cash')

    def test_get_orders_authenticated(self):
        url = reverse('orders-list')
        headers = {'Authorization': f'Token {self.token}'}
        response = self.client.get(url, headers=headers)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['status'], 'in_process')

    def test_filter_orders_by_finished(self):
        url = reverse('orders-list')
        headers = {'Authorization': f'Token {self.token}'}
        query_params = {'is_finished': 'true'}
        response = self.client.get(url, query_params, headers=headers)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 0)

    def test_filter_orders_by_cancelled(self):
        url = reverse('orders-list')
        headers = {'Authorization': f'Token {self.token}'}
        query_params = {'is_cancelled': 'true'}
        response = self.client.get(url, query_params, headers=headers)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 0)

    def test_filter_orders_by_current(self):
        url = reverse('orders-list')
        headers = {'Authorization': f'Token {self.token}'}
        query_params = {'is_current': 'true'}
        response = self.client.get(url, query_params, headers=headers)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)


class CreateOrderTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create(email='testuser@example.com', first_name='Іван', last_name='Іванов',
                                        phone_number='0676542345')
        self.token = Token.objects.create(user=self.user).key
        self.product1 = Product.objects.get(id=1)
        self.product1.quantity = 20
        self.product1.save()
        self.cart1 = Cart.objects.create(user=self.user)
        self.cart2 = Cart.objects.create(user=None)
        self.cart_item1 = CartItem.objects.create(product=self.product1, cart=self.cart1, quantity=2)
        self.cart_item2 = CartItem.objects.create(product=self.product1, cart=self.cart2, quantity=2)

    def test_create_order(self):
        url = reverse('create_order')
        data = {
            "payment_type": "cash",
            "warehouse_index": "55/145",
            "city_ref": "db5c88d0-391c-11dd-90d9-001a92567626"
        }
        headers = {'Authorization': f'Token {self.token}'}
        response = self.client.post(url, headers=headers, data=data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        time.sleep(20)  # need to let NOVA POST API save data

        res = NP.internet_document.delete(Order.objects.filter(user=self.user).last().document_ref)
        self.assertEqual(res['success'], True)

    def test_create_order_unregistered(self):
        url = reverse('create_order')
        data = {
            "payment_type": "cash",
            "warehouse_index": "55/145",
            "city_ref": "db5c88d0-391c-11dd-90d9-001a92567626",
            "first_name": "Іван",
            "last_name": "Іванов",
            "phone": "0676542345",
            "email": "test@example.com"

        }
        headers = {'Cart': f'Token {HashCode.objects.get(cart=self.cart2).key}'}
        response = self.client.post(url, headers=headers, data=data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        time.sleep(20)  # need to let NOVA POST API save data

        res = NP.internet_document.delete(Order.objects.order_by('id').last().document_ref)
        self.assertEqual(res['success'], True)

    def test_create_order_with_online_payment(self):
        url = reverse('create_order')
        data = {
            "payment_type": "online",
            "warehouse_index": "55/145",
            "city_ref": "db5c88d0-391c-11dd-90d9-001a92567626",
            "first_name": "Іван",
            "last_name": "Іванов",
            "phone": "0676542345",
            "email": "test@example.com"

        }
        headers = {'Cart': f'Token {HashCode.objects.get(cart=self.cart2).key}'}
        response = self.client.post(url, headers=headers, data=data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertNotEqual(response.data['checkout_url'], None)

    def test_create_order_empty_cart(self):
        self.cart_item1.delete()
        url = reverse('create_order')
        data = {
            "payment_type": "cash",
            "warehouse_index": "55/145",
            "city_ref": "db5c88d0-391c-11dd-90d9-001a92567626"
        }
        headers = {'Authorization': f'Token {self.token}'}
        response = self.client.post(url, headers=headers, data=data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class NPTestCase(APITestCase):

    def test_get_warehouse_types(self):
        url = reverse('get-warehouse-types')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        warehouse_types = NP.address.get_warehouse_types()
        self.assertEqual(warehouse_types['data'], response.data)

    def test_get_areas(self):
        url = reverse('get-settlement-areas')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        areas = NP.address.get_settlement_areas('')
        self.assertEqual(areas['data'], response.data)

    def test_get_settlements(self):
        areas = NP.address.get_settlement_areas('')
        area_ref = areas['data'][0]['Ref']
        url = reverse('get-settlements') + f'?area_ref={area_ref}'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        settlements = NP.address.get_settlements(area_ref=area_ref, warehouse=True, limit=5000, page=1)
        self.assertEqual(settlements['data'], response.data)

    def test_get_settlements_no_area_ref(self):
        url = reverse('get-settlements')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['error'], '"area_ref" is required')

    def test_get_warehouses(self):
        areas = NP.address.get_settlement_areas('')
        settlements = NP.address.get_settlements(area_ref=areas['data'][2]['Ref'], warehouse=True, limit=5000, page=1)
        settlement_ref = settlements['data'][0]['Ref']
        url = reverse('get-warehouses') + f'?settlement_ref={settlement_ref}'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        sleep(5)
        warehouses = NP.address.get_warehouses(settlement_ref=settlement_ref, limit=5000, page=1)
        self.assertEqual(warehouses['data'], response.data)

    def test_get_warehouses_no_settlement_ref(self):
        url = reverse('get-warehouses')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['error'], '"settlement_ref" is required')
