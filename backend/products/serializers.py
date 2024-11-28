from django.conf import settings
from django.db.models import Prefetch, F
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
        if not hasattr(obj, 'filtered_images') or not obj.filtered_images:
            return None
        main_image = obj.filtered_images[0]
        image = ProductImagesSerializer(main_image).data['image']
        base_url = settings.BASE_IMAGE_URL
        return f'{base_url}{image}' if base_url else image

    def get_discount_price(self, obj):
        if obj.price:
            try:
                discount_price = obj.discount_price
            except AttributeError:
                discount_price = obj.price - ((obj.price / 100) * obj.discount)

            return '{:.2f}'.format(discount_price)

    class Meta:
        model = Product
        fields = ['id', 'name', 'categories', 'price', 'discount', 'discount_price', 'changeable_prices', 'images',
                  'description']


class ProductDetailSerializer(ProductSerializer):
    brand = BrandSerializer(many=False, read_only=True)
    additional_fields = AdditionalFieldsSerializer(many=True, read_only=True)
    recommended_products = serializers.SerializerMethodField()
    images = ProductImagesSerializer(many=True, read_only=True)

    def get_recommended_products(self, obj):
        recommended_products = Product.objects.filter(subcategory=obj.subcategory).exclude(id=obj.id)[
                               :10].prefetch_related('changeable_prices', Prefetch('images',
                                                                                            queryset=ProductImages.objects.filter(
                                                                                                order=1),
                                                                                            to_attr='filtered_images')).select_related(
                'subcategory', 'subcategory__product_category', 'subcategory__product_category__animal_category',
                'brand').annotate(
                discount_price=F('price') - (F('price') * F('discount') / 100))
        serializer_object = ProductSerializer(recommended_products, many=True)
        return serializer_object.data

    class Meta:
        model = Product
        fields = ['id', 'name', 'categories', 'price', 'discount', 'discount_price', 'changeable_prices', 'is_new',
                  'images',
                  'description',
                  'additional_fields', 'brand', 'recommended_products']
