from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

from categories.models import SubCategory


class Brand(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False, unique=True)
    country = models.CharField(max_length=40, null=False, blank=False, unique=True)

    class Meta:
        verbose_name_plural = "brand"
        verbose_name = "brands"

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=256, null=False, blank=False, unique=True)
    subcategory = models.ForeignKey(SubCategory, on_delete=models.SET_NULL, null=True, blank=True)
    price = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
    sale = models.PositiveSmallIntegerField(default=0, validators=[
        MinValueValidator(0, message='Sale cannot be negative.'),
        MaxValueValidator(100, message='Sale cannot be greater than 100.')
    ])
    is_new = models.BooleanField(default=True)
    quantity = models.PositiveIntegerField(default=0,
                                           validators=[MinValueValidator(0, message='Quantity cannot be negative')])
    description = models.TextField(null=True, blank=True)
    brand = models.ForeignKey(Brand, on_delete=models.PROTECT, null=True, blank=True)

    class Meta:
        verbose_name_plural = "product"
        verbose_name = "products"

    def __str__(self):
        return f'{self.name} - {self.brand}'


class ChangeablePrice(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=False, blank=False,
                                related_name='changeable_prices')
    length = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
    width = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
    height = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
    weight = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
    size = models.CharField(max_length=50, null=True, blank=True)
    volume = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
    price = models.DecimalField(max_digits=7, decimal_places=2, null=False, blank=False)
    sale = models.PositiveSmallIntegerField(default=0, validators=[
        MinValueValidator(0, message='Sale cannot be negative.'),
        MaxValueValidator(100, message='Sale cannot be greater than 100.')
    ])
    order = models.PositiveSmallIntegerField(null=True, blank=True)

    class Meta:
        verbose_name_plural = "changeable price"
        verbose_name = "changeable prices"
        ordering = ['order']

    def __str__(self):
        product_name = self.product.name
        price = f"Price: {self.price}"
        additional_info = ""

        if self.volume is not None: # must be exactly this condition(if changed in would be 0 but not None)
            additional_info = f"Volume: {self.volume}"
        elif self.size:
            additional_info = f"Size: {self.size}"
        elif self.weight is not None: # must be exactly this condition
            additional_info = f"Weight: {self.weight}"
        elif all((self.length, self.width, self.height)):
            additional_info = f"{self.length} x {self.width} x {self.height}"

        return f"{product_name} - {additional_info} - {price}" if additional_info else f"{product_name} - NO DATA - {price}"


class ProductImages(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='product_images/', null=False, blank=False)
    order = models.PositiveSmallIntegerField(null=False, blank=False)

    class Meta:
        verbose_name_plural = "product image"
        verbose_name = "product images"
        ordering = ['order']

    def __str__(self):
        return f"{self.product.name} - Photo {self.order}"


class Tags(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='tags')
    title = models.CharField(max_length=256, null=False, blank=False)
    text = models.TextField(null=False, blank=False)

    class Meta:
        verbose_name_plural = "tag"
        verbose_name = "tags"
