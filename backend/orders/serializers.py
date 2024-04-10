from rest_framework import serializers

from orders.models import OrderItem, Order
from products.serializers import ProductSerializer, ChangeablePriceSerializer


class OrderItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer()
    changeable_price = ChangeablePriceSerializer()

    class Meta:
        model = OrderItem
        fields = ['id', 'product', 'quantity', 'changeable_price']


class OrderSerializer(serializers.ModelSerializer):
    order_items = OrderItemSerializer(many=True)

    class Meta:
        model = Order
        fields = ['id', 'status', 'payment_type', 'total_price', 'order_items', 'created_at', 'finished_at']
        read_only_fields = ['id', 'status', 'payment_type', 'created_at', 'finished_at', 'total_price']
