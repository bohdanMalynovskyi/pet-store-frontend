from django.db.models import Sum
from rest_framework import serializers, status

from categories.serializers import SubCategorySerializer
from products.models import Brand, ChangeablePrice, ProductImages, AdditionalFields, Product


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'


class ChangeablePriceSerializer(serializers.ModelSerializer):
    discount_price = serializers.SerializerMethodField()

    def get_discount_price(self, obj):
        discount_price = obj.price - ((obj.price / 100) * obj.discount)
        return '{:.2f}'.format(discount_price)

    class Meta:
        model = ChangeablePrice
        fields = ['id', 'price', 'discount', 'discount_price', 'length', 'width', 'height', 'weight', 'size', 'volume',
                  'quantity_in_pack']


class ProductImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImages
        fields = ['id', 'image']


class AdditionalFieldsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdditionalFields
        fields = ['id', 'title', 'text']


class ProductSerializer(serializers.ModelSerializer):
    changeable_prices = ChangeablePriceSerializer(many=True, read_only=True)
    images = serializers.SerializerMethodField()
    discount_price = serializers.SerializerMethodField()

    def get_images(self, obj):
        try:
            image_url = obj.images.get(order=1).image.url
            request = self.context.get('request')
            if request:
                return request.build_absolute_uri(image_url)
            else:
                return image_url
        except ProductImages.DoesNotExist:
            return None

    def get_discount_price(self, obj):
        if obj.price:
            try:
                discount_price = obj.discount_price
            except AttributeError:
                discount_price = obj.price - ((obj.price / 100) * obj.discount)

            return '{:.2f}'.format(discount_price)

    class Meta:
        model = Product
        fields = ['id', 'name', 'price', 'discount', 'discount_price', 'changeable_prices', 'images', 'description']


class ProductDetailSerializer(ProductSerializer):
    subcategory = SubCategorySerializer(many=False, read_only=True)
    brand = BrandSerializer(many=False, read_only=True)
    additional_fields = AdditionalFieldsSerializer(many=True, read_only=True)
    recommended_products = serializers.SerializerMethodField()
    images = ProductImagesSerializer(many=True, read_only=True)

    def get_recommended_products(self, obj):
        recommended_products = Product.objects.filter(subcategory=obj.subcategory).exclude(id=obj.id)[
                               :10].prefetch_related('changeable_prices', 'images')
        serializer_object = ProductSerializer(recommended_products, many=True)
        return serializer_object.data

    class Meta:
        model = Product
        fields = ['id', 'name', 'subcategory', 'price', 'discount', 'discount_price', 'changeable_prices', 'is_new',
                  'images',
                  'description',
                  'additional_fields', 'brand', 'recommended_products']
