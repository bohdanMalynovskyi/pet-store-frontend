from django.db.models import F
from django.urls import reverse
from rest_framework import status

from categories.tests.test_api import SubCategoryTestCase
from products.models import Brand, Product, ChangeablePrice, AdditionalFields
from products.serializers import ProductSerializer, ChangeablePriceSerializer, AdditionalFieldsSerializer, \
    ProductDetailSerializer


class ProductTestCase(SubCategoryTestCase):
    def setUp(self):
        super().setUp()
        self.brand = Brand.objects.create(name='Purina', country='United States')
        self.product = Product.objects.create(name='ProPlan', subcategory=self.subcategory1, discount=50, price=100,
                                              description='cool', brand=self.brand, weight=1)

    def test_get_list(self):
        """The problem arises from the fact that the serializer_data contains only relative paths(due to test environment) for images,
        while the response.data provides absolute paths. To address this discrepancy, we extract and compare only the relative paths in the test,
        ignoring the domain and protocol. This ensures a consistent and accurate comparison between the serializer and response data."""

        url = reverse('products-list')
        products = Product.objects.all()[:10]
        response = self.client.get(url)
        serializer_data = ProductSerializer(products, many=True).data

        # Extract relative paths from response.data
        for product in response.data['results']:
            for image in product.get('images', []):
                # Remove the domain and protocol, keep only relative paths
                image['image'] = image['image'].removeprefix('http://testserver')

        # Compare the serialized data and response data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.data['results'])

    def test_get_detail(self):
        url = reverse('products-detail', args=(self.product.id,))
        response = self.client.get(url)
        serializer_data = ProductDetailSerializer(self.product, ).data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.data)

    def test_get_detail_not_found(self):
        url = reverse('products-detail', args=(122,))
        response = self.client.get(url)
        self.assertEqual(status.HTTP_404_NOT_FOUND, response.status_code)
        self.assertEqual({"detail": "Not found."}, response.data)

    def test_post_detail_not_allowed(self):
        url = reverse('products-list')
        response = self.client.post(url)
        self.assertEqual(status.HTTP_405_METHOD_NOT_ALLOWED, response.status_code)
        self.assertEqual({"detail": "Method \"POST\" not allowed."}, response.data)

    def test_search_product_by_name(self):
        url = reverse('products-list')
        search_query = 'ProPlan'
        response = self.client.get(url, {'search': search_query})
        serializer_data = ProductSerializer(self.product).data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.data['results'][0])

    def test_search_product_by_description(self):
        url = reverse('products-list')
        search_query = 'cool'
        response = self.client.get(url, {'search': search_query})
        serializer_data = ProductSerializer(self.product).data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.data['results'][0])

    def test_sort_by_discount_price_ascending(self):
        """Test sorting products by discount price in ascending order."""
        url = reverse('products-list')
        response = self.client.get(url, {'ordering': 'price'})
        for product in response.data['results']:
            for image in product.get('images', []):
                # Remove the domain and protocol, keep only relative paths
                image['image'] = image['image'].removeprefix('http://testserver')
        sorted_products = Product.objects.all().annotate(
            discount_price=F('price') - (F('price') * F('discount') / 100)
        ).order_by('discount_price')[:10]
        serializer_data = ProductSerializer(sorted_products, many=True).data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.data['results'])

    def test_sort_by_discount_price_descending(self):
        """Test sorting products by discount price in descending order."""
        url = reverse('products-list')
        response = self.client.get(url, {'ordering': '-price'})
        for product in response.data['results']:
            for image in product.get('images', []):
                # Remove the domain and protocol, keep only relative paths
                image['image'] = image['image'].removeprefix('http://testserver')
        sorted_products = Product.objects.all().annotate(
            discount_price=F('price') - (F('price') * F('discount') / 100)
        ).order_by('-discount_price')[:10]
        serializer_data = ProductSerializer(sorted_products, many=True).data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.data['results'])

    def test_filter_by_min_price(self):
        url = reverse('products-list')
        min_price = 5  # Устанавливаем минимальную цену для фильтрации
        response = self.client.get(url, {'min_price': min_price})
        for product in response.data['results']:
            for image in product.get('images', []):
                # Remove the domain and protocol, keep only relative paths
                image['image'] = image['image'].removeprefix('http://testserver')
        filtered_products = Product.objects.annotate(
            discount_price=F('price') - (F('price') * F('discount') / 100)
        ).filter(discount_price__gte=min_price)[:10]
        serializer_data = ProductSerializer(filtered_products, many=True).data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.data['results'])

    # Дополненный тест для фильтрации по максимальной цене
    def test_filter_by_max_price(self):
        url = reverse('products-list')
        max_price = 150  # Устанавливаем максимальную цену для фильтрации
        response = self.client.get(url, {'max_price': max_price})
        for product in response.data['results']:
            for image in product.get('images', []):
                # Remove the domain and protocol, keep only relative paths
                image['image'] = image['image'].removeprefix('http://testserver')
        filtered_products = Product.objects.annotate(
            discount_price=F('price') - (F('price') * F('discount') / 100)
        ).filter(discount_price__lte=max_price)[:10]
        serializer_data = ProductSerializer(filtered_products, many=True).data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.data['results'])

    # Дополненный тест для фильтрации по подкатегории
    def test_filter_by_subcategory(self):
        url = reverse('products-list')
        response = self.client.get(url, {'subcategory': 1})
        for product in response.data['results']:
            for image in product.get('images', []):
                # Remove the domain and protocol, keep only relative paths
                image['image'] = image['image'].removeprefix('http://testserver')
        filtered_products = Product.objects.filter(subcategory_id=1)[:10]
        serializer_data = ProductSerializer(filtered_products, many=True).data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.data['results'])

    # Дополненный тест для фильтрации по категории животного
    def test_filter_by_animal_category(self):
        url = reverse('products-list')
        response = self.client.get(url, {'animal_category': 1})
        for product in response.data['results']:
            for image in product.get('images', []):
                # Remove the domain and protocol, keep only relative paths
                image['image'] = image['image'].removeprefix('http://testserver')
        filtered_products = Product.objects.filter(subcategory__product_category__animal_category_id=1)[:10]
        serializer_data = ProductSerializer(filtered_products, many=True).data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.data['results'])

    # Дополненный тест для фильтрации по категории продукта
    def test_filter_by_product_category(self):
        url = reverse('products-list')
        response = self.client.get(url, {'product_category': 1})
        for product in response.data['results']:
            for image in product.get('images', []):
                # Remove the domain and protocol, keep only relative paths
                image['image'] = image['image'].removeprefix('http://testserver')
        filtered_products = Product.objects.filter(subcategory__product_category_id=1)[:10]
        serializer_data = ProductSerializer(filtered_products, many=True).data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.data['results'])


class ChangeablePriceTestCase(ProductTestCase):
    def setUp(self):
        super().setUp()
        self.changeable_price = ChangeablePrice.objects.create(price=100, discount=50, product=self.product, order=1,
                                                               size='S')

    def test_get_list(self):
        url = reverse('changeableprices-list')
        changeable_prices = ChangeablePrice.objects.all()
        response = self.client.get(url)
        serializer_data = ChangeablePriceSerializer(changeable_prices, many=True).data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.data)

    def test_get_detail(self):
        url = reverse('changeableprices-detail', args=(self.changeable_price.id,))
        response = self.client.get(url)
        serializer_data = ChangeablePriceSerializer(self.changeable_price, ).data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.data)

    def test_get_detail_not_found(self):
        url = reverse('changeableprices-detail', args=(122,))
        response = self.client.get(url)
        self.assertEqual(status.HTTP_404_NOT_FOUND, response.status_code)
        self.assertEqual({"detail": "Not found."}, response.data)

    def test_post_detail_not_allowed(self):
        url = reverse('changeableprices-list')
        response = self.client.post(url)
        self.assertEqual(status.HTTP_405_METHOD_NOT_ALLOWED, response.status_code)
        self.assertEqual({"detail": "Method \"POST\" not allowed."}, response.data)

    def test_search_product_by_name(self):
        pass

    def test_search_product_by_description(self):
        pass


class AdditionalFieldsTestCase(ProductTestCase):
    def setUp(self):
        super().setUp()
        self.tag = AdditionalFields.objects.create(title='title', product=self.product, text='text')

    def test_get_list(self):
        url = reverse('additionaldata-list')
        additionaldata = AdditionalFields.objects.all()
        response = self.client.get(url)
        serializer_data = AdditionalFieldsSerializer(additionaldata, many=True).data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.data)

    def test_get_detail(self):
        url = reverse('additionaldata-detail', args=(self.tag.id,))
        response = self.client.get(url)
        serializer_data = AdditionalFieldsSerializer(self.tag, ).data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.data)

    def test_get_detail_not_found(self):
        url = reverse('additionaldata-detail', args=(122,))
        response = self.client.get(url)
        self.assertEqual(status.HTTP_404_NOT_FOUND, response.status_code)
        self.assertEqual({"detail": "Not found."}, response.data)

    def test_post_detail_not_allowed(self):
        url = reverse('additionaldata-list')
        response = self.client.post(url)
        self.assertEqual(status.HTTP_405_METHOD_NOT_ALLOWED, response.status_code)
        self.assertEqual({"detail": "Method \"POST\" not allowed."}, response.data)

    def test_search_product_by_name(self):
        pass

    def test_search_product_by_description(self):
        pass
