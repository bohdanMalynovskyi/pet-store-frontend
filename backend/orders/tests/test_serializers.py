from orders.models import Order, OrderItem
from orders.serializers import OrderItemSerializer, OrderSerializer
from products.tests.test_serializers import ProductsTests
from users.models import HashCode


class OrderItemSerializerTest(ProductsTests):

    def setUp(self):
        super().setUp()
        self.order = Order.objects.create(status='in_process', payment_type='cash')
        self.order_item1 = OrderItem.objects.create(product=self.product, order=self.order, quantity=1, fixed_price=50)

    def test_ok(self):
        expected_data = {
            'id': self.order_item1.id,
            'product': {
                'id': self.product.id,
                'name': 'ProPlan',
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
        data = OrderItemSerializer(self.order_item1).data
        self.assertEqual(expected_data, data)


class OrderSerializerTest(OrderItemSerializerTest):
    def setUp(self):
        super().setUp()

    def test_ok(self):
        serializer = OrderItemSerializer(self.order_item1)

        data = OrderSerializer(self.order).data
        expected_data = {
            'id': self.order.id,
            'status': 'in_process',
            'payment_type': 'cash',
            'total_price': None,
            'order_items': [serializer.data],
            'created_at': data['created_at'],
            'finished_at': None
        }
        self.assertEqual(expected_data, data)
