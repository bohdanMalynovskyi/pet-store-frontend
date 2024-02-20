from rest_framework import serializers

from products.serializers import ProductSerializer
from users.models import Cart, CartItem, FeaturedProducts, FeaturedItem


class CartItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer()

    class Meta:
        model = CartItem
        fields = ['id', 'product', 'quantity']


class CartSerializer(serializers.ModelSerializer):
    cart_items = CartItemSerializer(many=True, read_only=True)

    class Meta:
        model = Cart
        fields = ['id', 'hash_code', 'cart_items']
        read_only_fields = ['hash_code']


class FeaturedItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer()

    class Meta:
        model = FeaturedItem
        fields = ['id', 'product']


class FeaturedProductsSerializer(serializers.ModelSerializer):
    featured_items = FeaturedItemSerializer(many=True, read_only=True)

    class Meta:
        model = FeaturedProducts
        fields = ['id', 'hash_code', 'featured_items']
        read_only_fields = ['hash_code']
