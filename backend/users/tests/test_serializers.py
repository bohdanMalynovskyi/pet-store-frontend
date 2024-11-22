from unittest import TestCase

from django.contrib.auth.hashers import check_password

from products.serializers import ProductSerializer
from products.tests.test_serializers import ProductsTests
from users.models import Cart, CartItem, FeaturedProducts, FeaturedItem, User, HashCode
from users.serializers import CartItemSerializer, CartSerializer, FeaturedItemSerializer, FeaturedProductsSerializer, \
    CustomUserSerializer, CustomUserCreateRetypeSerializer


class CartItemSerializerTest(ProductsTests):

    def setUp(self):
        super().setUp()
        self.cart = Cart.objects.create()
        self.cart_item1 = CartItem.objects.create(product=self.product, cart=self.cart, quantity=1)

    def test_ok(self):
        product_serializer = ProductSerializer()
        categories = product_serializer.get_categories(self.product)
        expected_data = {
            'id': self.cart_item1.id,
            'product': {
                'id': self.product.id,
                'name': 'ProPlan',
                'categories': categories,
                'price': '100.00',
                'discount': 50,
                'discount_price': '50.00',
                'changeable_prices': [],
                'images': None,
                'description': 'cool'
            },
            'quantity': 1,
            'changeable_price': None
        }
        data = CartItemSerializer(self.cart_item1).data
        self.assertEqual(expected_data, data)


class CartSerializerTest(CartItemSerializerTest):

    def setUp(self):
        super().setUp()

    def test_ok(self):
        serializer = CartItemSerializer(self.cart_item1)
        expected_data = {
            'id': self.cart.id,
            'hash_code': self.cart.hash_code.key,
            'cart_items': [serializer.data]
        }

        data = CartSerializer(self.cart).data
        self.assertEqual(expected_data, data)


class FeaturedItemSerializerTest(ProductsTests):

    def setUp(self):
        super().setUp()
        self.featured = FeaturedProducts.objects.create()
        self.featured_item1 = FeaturedItem.objects.create(product=self.product, featured_products=self.featured)

    def test_ok(self):
        product_serializer = ProductSerializer()
        categories = product_serializer.get_categories(self.product)
        expected_data = {
            'id': self.featured_item1.id,
            'product': {
                'id': self.product.id,
                'name': 'ProPlan',
                'categories': categories,
                'price': '100.00',
                'discount': 50,
                'discount_price': '50.00',
                'changeable_prices': [],
                'images': None,
                'description': 'cool'
            },
            'changeable_price': None
        }
        data = FeaturedItemSerializer(self.featured_item1).data
        self.assertEqual(expected_data, data)


class FeaturedProductSerializerTest(FeaturedItemSerializerTest):

    def setUp(self):
        super().setUp()

    def test_ok(self):
        serializer = FeaturedItemSerializer(self.featured_item1)
        expected_data = {
            'id': self.featured.id,
            'hash_code': self.featured.hash_code.key,
            'featured_items': [serializer.data]
        }
        data = FeaturedProductsSerializer(self.featured).data
        self.assertEqual(expected_data, data)


class CustomUserSerializerTest(TestCase):
    def setUp(self):
        self.user_data = {
            'email': 'test1@example.com',
            'password': 'testpassword',
            'first_name': 'Олександр',
            'second_name': 'Олександрович',
            'last_name': 'Олександренко',
            'phone_number': '0682862345',
        }
        self.user = User.objects.create(**self.user_data)

    def test_serialization(self):
        serializer = CustomUserSerializer(instance=self.user)
        expected_data = {
            'id': self.user.id,
            'email': 'test1@example.com',
            'first_name': 'Олександр',
            'second_name': 'Олександрович',
            'last_name': 'Олександренко',
            'phone_number': '0682862345',
        }
        self.assertEqual(serializer.data, expected_data)


class CustomUserCreateSerializerTest(TestCase):
    def setUp(self):
        self.user_data = {
            'email': 'test2@example.com',
            'password': 'testpassword',
            're_password': 'testpassword',
            'first_name': 'Олександр',
            'second_name': 'Олександрович',
            'last_name': 'Олександренко',
            'phone_number': '0682862345'
        }

    def test_create_serialization(self):
        serializer = CustomUserCreateRetypeSerializer(data=self.user_data)
        self.assertTrue(serializer.is_valid())
        saved_user = serializer.save()
        self.assertEqual(saved_user.email, 'test2@example.com')
        self.assertTrue(check_password('testpassword', saved_user.password))
        self.assertEqual(saved_user.first_name, 'Олександр')
        self.assertEqual(saved_user.second_name, 'Олександрович')
        self.assertEqual(saved_user.last_name, 'Олександренко')
        self.assertEqual(saved_user.phone_number, '0682862345')
