from django.urls import reverse
from rest_framework import status
from rest_framework.authtoken.models import Token

from products.models import Product, ChangeablePrice
from users.logic import get_cart, get_featured

from users.models import Cart, CartItem, FeaturedProducts, FeaturedItem, User
from users.serializers import CartSerializer, FeaturedProductsSerializer
from rest_framework.test import APITestCase


class CartTestCase(APITestCase):
    fixtures = ['base_data.json']

    def test_create_cart(self):
        url = reverse('create-cart')
        response = self.client.post(url)

        cart = Cart.objects.last()
        serializer = CartSerializer(cart)
        self.assertEqual(cart.user, None)
        self.assertEqual(status.HTTP_201_CREATED, response.status_code)
        self.assertEqual(serializer.data, response.data)

    def test_create_cart_with_user(self):
        url = reverse('create-cart')
        user = User.objects.create(email='tomatoma1234@gmail.com')
        token = Token.objects.create(user=user).key
        headers = {'Authorization': f'Token {token}'}
        response = self.client.post(url, headers=headers)

        cart = Cart.objects.last()
        serializer = CartSerializer(cart)

        self.assertEqual(cart.user, user)
        self.assertEqual(status.HTTP_201_CREATED, response.status_code)
        self.assertEqual(serializer.data, response.data)

    def setUp(self):
        self.user = User.objects.create(email='tomatoma123@gmail.com')
        self.token = Token.objects.create(user=self.user).key
        self.product1 = Product.objects.get(id=1)
        self.product2 = Product.objects.get(id=3)
        self.product3 = Product.objects.get(id=2)
        self.cart1 = Cart.objects.create()
        self.cart2 = Cart.objects.create(user=self.user)
        self.cart3 = Cart.objects.create()
        self.cart_item1 = CartItem.objects.create(product=self.product1, cart=self.cart1, quantity=2)
        self.cart_item2 = CartItem.objects.create(product=self.product1, cart=self.cart2, quantity=2)
        self.cart_item3 = CartItem.objects.create(product=self.product3, cart=self.cart3, quantity=1)

    def test_get_cart(self):
        url = reverse('get-cart')
        headers = {'Cart': f'Token {self.cart1.hash_code.key}'}
        response = self.client.get(url, headers=headers)

        cart = get_cart(self.cart1.id)

        serializer = CartSerializer(cart)

        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer.data, response.data)

    def test_get_cart_with_user(self):
        url = reverse('get-cart')
        headers = {'Authorization': f'Token {self.token}'}
        response = self.client.get(url, headers=headers)

        cart = get_cart(self.cart2.id)

        serializer = CartSerializer(cart)

        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer.data, response.data)

    def test_add_to_cart(self):
        url = reverse('add-to-cart', args=[self.product2.id])
        headers = {'Cart': f'Token {self.cart1.hash_code.key}'}
        self.client.post(url, headers=headers)

        self.assertEqual(self.cart1.cart_items.last().quantity, 1)

        response = self.client.post(url, headers=headers)
        cart = get_cart(self.cart1.id)

        serializer = CartSerializer(cart)
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer.data, response.data)
        self.assertEqual(self.cart1.cart_items.last().quantity, 2)

    def test_change_cart_item_changeable_price(self):
        url = reverse('change-cart-changeable-price', args=[self.product3.id, ChangeablePrice.objects.all()[0].id])
        headers = {'Cart': f'Token {self.cart3.hash_code.key}'}
        response = self.client.post(url, headers=headers)

        self.assertEqual(self.cart3.cart_items.last().changeable_price.id, ChangeablePrice.objects.all()[0].id)
        cart = get_cart(self.cart3.id)

        serializer = CartSerializer(cart)
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer.data, response.data)

    def test_add_to_cart_with_user(self):
        url = reverse('add-to-cart', args=[self.product2.id])
        headers = {'Authorization': f'Token {self.token}'}
        self.client.post(url, headers=headers)

        self.cart2.refresh_from_db()

        self.assertEqual(self.cart2.cart_items.last().quantity, 1)

        response = self.client.post(url, headers=headers)

        cart = get_cart(self.cart2.id)

        serializer = CartSerializer(cart)
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer.data, response.data)
        self.assertEqual(self.cart2.cart_items.last().quantity, 2)

    def test_decrease_cart_item(self):
        url = reverse('decrease-quantity', args=[self.product1.id])
        headers = {'Cart': f'Token {self.cart1.hash_code.key}'}
        self.client.post(url, headers=headers)

        self.cart1.refresh_from_db()
        self.assertEqual(self.cart1.cart_items.last().quantity, 1)

        response = self.client.post(url, headers=headers)

        serializer = CartSerializer(self.cart1)

        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer.data, response.data)
        self.assertEqual(self.cart1.cart_items.count(), 0)

    def test_decrease_cart_item_with_user(self):
        url = reverse('decrease-quantity', args=[self.product1.id])
        headers = {'Authorization': f'Token {self.token}'}
        self.client.post(url, headers=headers)

        self.cart2.refresh_from_db()
        self.assertEqual(self.cart2.cart_items.last().quantity, 1)

        response = self.client.post(url, headers=headers)

        serializer = CartSerializer(self.cart2)

        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer.data, response.data)
        self.assertEqual(self.cart2.cart_items.count(), 0)

    def test_delete_cart_item(self):
        url = reverse('delete-cart-item', args=[self.product1.id])
        headers = {'Cart': f'Token {self.cart1.hash_code.key}'}
        response = self.client.delete(url, headers=headers)

        serializer = CartSerializer(self.cart1)

        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer.data, response.data)
        self.assertEqual(self.cart1.cart_items.count(), 0)

    def test_delete_cart_item_with_user(self):
        url = reverse('delete-cart-item', args=[self.product1.id])
        headers = {'Authorization': f'Token {self.token}'}
        response = self.client.delete(url, headers=headers)

        serializer = CartSerializer(self.cart2)

        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer.data, response.data)
        self.assertEqual(self.cart2.cart_items.count(), 0)

    def test_clear_cart(self):
        url = reverse('clear-cart')
        headers = {'Cart': f'Token {self.cart1.hash_code.key}'}
        response = self.client.post(url, headers=headers)

        serializer = CartSerializer(self.cart1)

        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer.data, response.data)
        self.assertEqual(self.cart1.cart_items.count(), 0)

    def test_clear_cart_with_user(self):
        url = reverse('clear-cart')
        headers = {'Authorization': f'Token {self.token}'}
        response = self.client.post(url, headers=headers)

        serializer = CartSerializer(self.cart2)

        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer.data, response.data)
        self.assertEqual(self.cart2.cart_items.count(), 0)


class FeaturedTestCase(APITestCase):
    fixtures = ['base_data.json']

    def test_create_featured(self):
        url = reverse('create-featured')
        response = self.client.post(url)

        featured = FeaturedProducts.objects.last()
        serializer = FeaturedProductsSerializer(featured)
        self.assertEqual(featured.user, None)
        self.assertEqual(status.HTTP_201_CREATED, response.status_code)
        self.assertEqual(serializer.data, response.data)

    def test_create_featured_with_user(self):
        url = reverse('create-featured')
        user = User.objects.create(email='tomatoma1234@gmail.com')
        token = Token.objects.create(user=user).key
        headers = {'Authorization': f'Token {token}'}
        response = self.client.post(url, headers=headers)

        featured = FeaturedProducts.objects.last()
        serializer = FeaturedProductsSerializer(featured)

        self.assertEqual(featured.user, user)
        self.assertEqual(status.HTTP_201_CREATED, response.status_code)
        self.assertEqual(serializer.data, response.data)

    def setUp(self):
        self.user = User.objects.create(email='tomatoma123@gmail.com')
        self.token = Token.objects.create(user=self.user).key
        self.product1 = Product.objects.get(id=1)
        self.product2 = Product.objects.get(id=3)
        self.product3 = Product.objects.get(id=2)
        self.featured1 = FeaturedProducts.objects.create()
        self.featured2 = FeaturedProducts.objects.create(user=self.user)
        self.featured3 = FeaturedProducts.objects.create()
        self.featured_item1 = FeaturedItem.objects.create(product=self.product1, featured_products=self.featured1)
        self.featured_item2 = FeaturedItem.objects.create(product=self.product1, featured_products=self.featured2)
        self.featured_item3 = FeaturedItem.objects.create(product=self.product1, featured_products=self.featured3)

    def test_get_featured(self):
        url = reverse('get-featured')
        headers = {'Featured': f'Token {self.featured1.hash_code.key}'}
        response = self.client.get(url, headers=headers)
        featured = get_featured(self.featured1.id)

        serializer = FeaturedProductsSerializer(featured)
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer.data, response.data)

    def test_get_featured_with_user(self):
        url = reverse('get-featured')
        headers = {'Authorization': f'Token {self.token}'}
        response = self.client.get(url, headers=headers)

        featured = get_featured(self.featured2.id)

        serializer = FeaturedProductsSerializer(featured)

        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer.data, response.data)

    def test_add_to_featured(self):
        url = reverse('add-to-featured', args=[self.product2.id])
        headers = {'Featured': f'Token {self.featured1.hash_code.key}'}
        response = self.client.post(url, headers=headers)
        featured = get_featured(self.featured1.id)

        serializer = FeaturedProductsSerializer(featured)
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer.data, response.data)
        self.assertEqual(self.featured1.featured_items.count(), 2)

    # def test_change_featured_item_changeable_price(self):
    #     url = reverse('change-featured-changeable-price', args=[self.product3.id, ChangeablePrice.objects.all()[0].id])
    #     headers = {'Featured': f'Token {self.featured3.hash_code.key}'}
    #     response = self.client.post(url, headers=headers)
    #
    #     self.assertEqual(self.featured3.featured_items.last().changeable_price.id, ChangeablePrice.objects.all()[0].id)
    #     featured = get_featured(self.featured3.id)
    #
    #     serializer = FeaturedProductsSerializer(featured)
    #     self.assertEqual(status.HTTP_200_OK, response.status_code)
    #     self.assertEqual(serializer.data, response.data)

    def test_add_to_featured_with_user(self):
        url = reverse('add-to-featured', args=[self.product2.id])
        headers = {'Authorization': f'Token {self.token}'}
        response = self.client.post(url, headers=headers)
        featured = get_featured(self.featured2.id)

        serializer = FeaturedProductsSerializer(featured)
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer.data, response.data)
        self.assertEqual(self.featured2.featured_items.count(), 2)

    def test_delete_featured_item(self):
        url = reverse('delete-featured-item', args=[self.product1.id])
        headers = {'Featured': f'Token {self.featured1.hash_code.key}'}
        response = self.client.delete(url, headers=headers)

        serializer = FeaturedProductsSerializer(self.featured1)

        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer.data, response.data)
        self.assertEqual(self.featured1.featured_items.count(), 0)

    def test_delete_featured_item_with_user(self):
        url = reverse('delete-featured-item', args=[self.product1.id])
        headers = {'Authorization': f'Token {self.token}'}
        response = self.client.delete(url, headers=headers)

        serializer = FeaturedProductsSerializer(self.featured2)

        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer.data, response.data)
        self.assertEqual(self.featured2.featured_items.count(), 0)

    def test_clear_featured(self):
        url = reverse('clear-featured')
        headers = {'Featured': f'Token {self.featured1.hash_code.key}'}
        response = self.client.post(url, headers=headers)

        serializer = FeaturedProductsSerializer(self.featured1)

        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer.data, response.data)
        self.assertEqual(self.featured1.featured_items.count(), 0)

    def test_clear_featured_with_user(self):
        url = reverse('clear-featured')
        headers = {'Authorization': f'Token {self.token}'}
        response = self.client.post(url, headers=headers)

        serializer = FeaturedProductsSerializer(self.featured2)

        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer.data, response.data)
        self.assertEqual(self.featured2.featured_items.count(), 0)


class CustomDjoserEndpointTests(APITestCase):
    fixtures = ['base_data.json']

    def setUp(self):
        self.user_data = {
            'email': 'test@example.com',
            'password': 'testpassword',
            'first_name': 'Олександр',
            'last_name': 'Олександренко',
            'phone_number': '0682862345'
        }
        self.user = User.objects.create_user(**self.user_data)
        self.login_url = reverse('login')
        self.logout_url = reverse('logout')
        self.user_detail_url = reverse('user-me')  # Assuming you have a user details endpoint

    def test_user_login(self):
        data = {'email': self.user_data['email'], 'password': 'testpassword'}
        response = self.client.post(self.login_url, data=data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('auth_token', response.data)

    def test_user_logout(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.post(self.logout_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_user_detail(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.get(self.user_detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['email'], self.user_data['email'])
        self.assertEqual(response.data['first_name'], self.user_data['first_name'])
        self.assertEqual(response.data['last_name'], self.user_data['last_name'])
        self.assertEqual(response.data['phone_number'], self.user_data['phone_number'])

    def test_user_registration(self):
        new_user_data = {
            'email': 'newuser@example.com',
            'password': 'newuserpassword',
            're_password': 'newuserpassword',
            'first_name': 'Олександр',
            'last_name': 'Олександренко',
            'phone_number': '0682862345'
        }
        response = self.client.post(reverse('user-list'), new_user_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 2)
        new_user = User.objects.get(email=new_user_data['email'])
        self.assertEqual(new_user.first_name, new_user_data['first_name'])
        self.assertEqual(new_user.last_name, new_user_data['last_name'])
        self.assertEqual(new_user.phone_number, new_user_data['phone_number'])
        self.assertEqual(new_user.is_active, False)

    def test_user_registration_with_cart_and_featured(self):
        cart = Cart.objects.create()
        featured = FeaturedProducts.objects.create()
        new_user_data = {
            'email': 'newuser@example.com',
            'password': 'newuserpassword',
            're_password': 'newuserpassword',
            'first_name': 'Олександр',
            'last_name': 'Олександренко',
            'phone_number': '0682862345',
            'cart_hash_code': f'{cart.hash_code.key}',
            'featured_hash_code': f'{featured.hash_code.key}'
        }
        response = self.client.post(reverse('user-list'), new_user_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 2)
        new_user = User.objects.get(email=new_user_data['email'])
        self.assertEqual(new_user.first_name, new_user_data['first_name'])
        self.assertEqual(new_user.last_name, new_user_data['last_name'])
        self.assertEqual(new_user.phone_number, new_user_data['phone_number'])
        cart.refresh_from_db()
        featured.refresh_from_db()
        self.assertEqual(new_user.cart.hash_code, None)
        self.assertEqual(cart.user, new_user)
        self.assertEqual(featured.user, new_user)
        self.assertEqual(new_user.featured.hash_code, None)
        self.assertEqual(new_user.is_active, False)
