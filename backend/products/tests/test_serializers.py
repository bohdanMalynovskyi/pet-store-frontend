from django.core.files.uploadedfile import SimpleUploadedFile

from categories.tests.test_serializers import SubCategoryTests
from products.models import Brand, Product, ChangeablePrice, AdditionalFields, ProductImages
from products.serializers import BrandSerializer, ProductSerializer, ChangeablePriceSerializer, \
    AdditionalFieldsSerializer, \
    ProductImagesSerializer, ProductDetailSerializer


class BrandTests(SubCategoryTests):

    def setUp(self):
        super().setUp()
        self.brand = Brand.objects.create(name='Purina', country='United States')

    def test_ok(self):
        expected_data = {
            'id': self.brand.id,
            'name': 'Purina',
            'country': 'United States'
        }
        data = BrandSerializer(self.brand).data
        self.assertEqual(expected_data, data)


class ProductsTests(BrandTests):

    def setUp(self):
        super().setUp()
        self.product = Product.objects.create(name='ProPlan', subcategory=self.sub_category, discount=50, price=100,
                                              description='cool', brand=self.brand, weight=1)

    def test_ok(self):
        expected_data = {
            'id': self.product.id,
            'name': 'ProPlan',
            'price': '100.00',
            'discount': 50,
            'discount_price': '50.00',
            'changeable_prices': [],
            'images': None,
            'description': 'cool'
        }
        data = ProductSerializer(self.product).data
        self.assertEqual(expected_data, data)


class ProductDetailTests(ProductsTests):

    def setUp(self):
        super().setUp()

    def test_ok(self):
        recommended_products = Product.objects.filter(subcategory=self.product.subcategory).exclude(id=self.product.id)[
                               :10]
        serializer_object = ProductSerializer(recommended_products, many=True)
        expected_data = {
            'id': self.product.id,
            'name': 'ProPlan',
            'subcategory': {
                'id': self.sub_category.id,
                'key': '',
                'name': 'Wet food'
            },
            'price': '100.00',
            'discount': 50,
            'discount_price': '50.00',
            'changeable_prices': [],
            'is_new': True,
            'images': [],
            'description': 'cool',
            'additional_fields': [],
            'brand': {
                'id': self.brand.id,
                'name': 'Purina',
                'country': 'United States'
            },
            'recommended_products': serializer_object.data
        }
        data = ProductDetailSerializer(self.product).data
        self.assertEqual(expected_data, data)


class ChangeablePriceTests(ProductDetailTests):
    def setUp(self):
        super().setUp()
        self.changeable_price = ChangeablePrice.objects.create(price=100, discount=50, product=self.product, order=1,
                                                               size='S')

    def test_ok(self):
        expected_data = {
            'id': self.changeable_price.id,
            'price': '100.00',
            'discount': 50,
            'discount_price': '50.00',
            'length': None,
            'width': None,
            'height': None,
            'weight': None,
            'size': 'S',
            'volume': None,
            'quantity_in_pack': None
        }
        data = ChangeablePriceSerializer(self.changeable_price).data
        self.assertEqual(expected_data, data)


class AdditionalFieldsSerializerTests(ProductDetailTests):
    def setUp(self):
        super().setUp()
        self.tag = AdditionalFields.objects.create(title='title', product=self.product, text='text')

    def test_ok(self):
        expected_data = {
            'id': self.tag.id,
            'title': 'title',
            'text': 'text',
        }
        data = AdditionalFieldsSerializer(self.tag).data
        self.assertEqual(expected_data, data)


class ProductImagesTests(ProductDetailTests):
    def setUp(self):
        super().setUp()
        self.image = SimpleUploadedFile("image.jpg", b"file_content", content_type="image/jpeg")
        self.product_image = ProductImages.objects.create(product=self.product, image=self.image, order=1)

    def test_ok(self):
        expected_data = {
            'id': self.product_image.id,
            'image': f'/media/{self.product_image.image.name}'
        }
        data = ProductImagesSerializer(self.product_image).data
        self.assertEqual(expected_data, data)
