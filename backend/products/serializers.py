from rest_framework import serializers

from categories.serializers import SubCategorySerializer
from products.models import Brand, ChangeablePrice, ProductImages, Tags, Product


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'


class ChangeablePriceSerializer(serializers.ModelSerializer):
    sale_price = serializers.SerializerMethodField()

    def get_sale_price(self, obj):
        return obj.price - ((obj.price / 100) * obj.sale)

    class Meta:
        model = ChangeablePrice
        fields = ['id', 'price', 'sale_price', 'sale', 'length', 'width', 'height', 'weight', 'size', 'volume']


class ProductImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImages
        fields = ['id', 'image']


class TagsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tags
        fields = ['id', 'title', 'text']


class ProductSerializer(serializers.ModelSerializer):
    brand = BrandSerializer(many=False, read_only=True)
    changeable_prices = ChangeablePriceSerializer(many=True, read_only=True)
    images = ProductImagesSerializer(many=True, read_only=True)
    tags = TagsSerializer(many=True, read_only=True)
    subcategory = SubCategorySerializer(many=False, read_only=True)
    sale_price = serializers.SerializerMethodField()

    def get_sale_price(self, obj):
        return obj.price - ((obj.price / 100) * obj.sale)

    class Meta:
        model = Product
        fields = ['id', 'name', 'subcategory', 'price', 'sale', 'sale_price', 'changeable_prices', 'is_new', 'images', 'description',
                  'tags', 'brand']
        # TODO CALCULATE PRICE WITH SALES
