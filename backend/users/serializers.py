from rest_framework import serializers

from products.serializers import ProductSerializer, ChangeablePriceSerializer
from users.models import Cart, CartItem, FeaturedProducts, FeaturedItem, User, HashCode

from djoser.serializers import UserCreateSerializer, UserSerializer, UserCreatePasswordRetypeSerializer


class CustomUserCreateRetypeSerializer(UserCreatePasswordRetypeSerializer):
    """
    Цей серіалізатор розширює UserCreatePasswordRetypeSerializer, щоб включити поля для
    cart_hash_code та featured_hash_code, що дозволяє приєднати кошик та обрані товари
    до користувача при створенні.
    """
    cart_hash_code = serializers.CharField(write_only=True, required=False)
    featured_hash_code = serializers.CharField(write_only=True, required=False)

    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = ('email', 'password', 'first_name', 'second_name', 'last_name',
                  'phone_number', 'cart_hash_code', 'featured_hash_code')

    def validate(self, attrs):
        cart_hash_code = attrs.pop('cart_hash_code', None)
        featured_hash_code = attrs.pop('featured_hash_code', None)
        attrs = super().validate(attrs)
        attrs['cart_hash_code'] = cart_hash_code
        attrs['featured_hash_code'] = featured_hash_code
        return attrs

    def create(self, validated_data):
        cart_hash_code = validated_data.pop('cart_hash_code', None)
        featured_hash_code = validated_data.pop('featured_hash_code', None)

        user = User.objects.create_user(**validated_data)

        if cart_hash_code:
            cart = Cart.objects.get(hash_code__key=cart_hash_code)
            cart.user = user
            cart.hash_code.delete()
            cart.hash_code = None
            cart.save()

        if featured_hash_code:
            featured = FeaturedProducts.objects.get(hash_code__key=featured_hash_code)
            featured.user = user
            featured.hash_code.delete()
            featured.hash_code = None
            featured.save()

        return user


class CustomUserSerializer(UserSerializer):
    class Meta(UserSerializer.Meta):
        model = User
        fields = (
            'id', 'email', 'first_name', 'second_name', 'last_name', 'phone_number')


class CartItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer()
    changeable_price = ChangeablePriceSerializer()

    class Meta:
        model = CartItem
        fields = ['id', 'product', 'quantity', 'changeable_price']


class HashCodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = HashCode
        fields = ['key']


class CartSerializer(serializers.ModelSerializer):
    cart_items = CartItemSerializer(many=True, read_only=True)
    hash_code = serializers.SerializerMethodField()

    def get_hash_code(self, obj):
        try:
            return obj.hash_code.key
        except AttributeError:
            return None

    class Meta:
        model = Cart
        fields = ['id', 'hash_code', 'cart_items']
        read_only_fields = ['hash_code']


class FeaturedItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer()
    changeable_price = ChangeablePriceSerializer()

    class Meta:
        model = FeaturedItem
        fields = ['id', 'product', 'changeable_price']


class FeaturedProductsSerializer(serializers.ModelSerializer):
    featured_items = FeaturedItemSerializer(many=True, read_only=True)
    hash_code = serializers.SerializerMethodField()

    def get_hash_code(self, obj):
        try:
            return obj.hash_code.key
        except AttributeError:
            return None

    class Meta:
        model = FeaturedProducts
        fields = ['id', 'hash_code', 'featured_items']
        read_only_fields = ['hash_code']
