from products.models import Product
from products.tests.test_serializers import ProductsTests
from users.models import Cart, CartItem, FeaturedProducts, FeaturedItem
from users.serializers import CartItemSerializer, CartSerializer, FeaturedItemSerializer, FeaturedProductsSerializer


class CartItemSerializerTest(ProductsTests):

    def setUp(self):
        super().setUp()
        self.cart = Cart.objects.create()
        self.cart_item1 = CartItem.objects.create(product=self.product, cart=self.cart, quantity=1)

    def test_ok(self):
        expected_data = {
            'id': self.cart_item1.id,
            'product': {
                'id': self.product.id,
                'name': 'ProPlan',
                'price': '100.00',
                'discount': 50,
                'discount_price': '50.00',
                'changeable_prices': [],
                'images': [],
                'description': 'cool'
            },
            'quantity': 1
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
            'hash_code': self.cart.hash_code,
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
        expected_data = {
            'id': self.featured_item1.id,
            'product': {
                'id': self.product.id,
                'name': 'ProPlan',
                'price': '100.00',
                'discount': 50,
                'discount_price': '50.00',
                'changeable_prices': [],
                'images': [],
                'description': 'cool'
            },
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
            'hash_code': self.featured.hash_code,
            'featured_items': [serializer.data]
        }
        data = FeaturedProductsSerializer(self.featured).data
        self.assertEqual(expected_data, data)
