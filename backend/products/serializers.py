from django.conf import settings
from rest_framework import serializers

from categories.serializers import SubCategorySerializer, SubCategoryHierarchySerializer, \
    AnimalCategoryHierarchySerializer, ProductCategoryHierarchySerializer
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
    categories = serializers.SerializerMethodField()

    def get_categories(self, obj):
        try:
            return {
                "animal_category": AnimalCategoryHierarchySerializer(
                    obj.subcategory.product_category.animal_category, many=False
                ).data,
                "product_category": ProductCategoryHierarchySerializer(
                    obj.subcategory.product_category, many=False
                ).data,
                "subcategory": SubCategoryHierarchySerializer(
                    obj.subcategory, many=False
                ).data,
            }
        except AttributeError:
            return None

    def get_images(self, obj):
        main_image = obj.images.filter(order=1).first()
        image = ProductImagesSerializer(main_image).data
        base_url = settings.BASE_IMAGE_URL
        image = image['image']
        if not base_url:
            return image
        if not image:
            return None
        return f'{base_url}{image}'

    def get_discount_price(self, obj):
        if obj.price:
            try:
                discount_price = obj.discount_price
            except AttributeError:
                discount_price = obj.price - ((obj.price / 100) * obj.discount)

            return '{:.2f}'.format(discount_price)

    class Meta:
        model = Product
        fields = ['id', 'name', 'categories', 'price','discount', 'discount_price', 'changeable_prices', 'images', 'description']


class ProductDetailSerializer(ProductSerializer):
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
        fields = ['id', 'name', 'categories', 'price', 'discount', 'discount_price', 'changeable_prices', 'is_new',
                  'images',
                  'description',
                  'additional_fields', 'brand', 'recommended_products']
