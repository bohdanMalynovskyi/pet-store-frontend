import hashlib
import random
from datetime import datetime

from django.core.validators import MinValueValidator
from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver

from products.models import Product


def generate_unique_hash():
    hash_code = hashlib.sha256(str(random.getrandbits(256)).encode('utf-8')).hexdigest()
    return hash_code


class Cart(models.Model):
    hash_code = models.CharField(max_length=64, unique=True)
    products = models.ManyToManyField(Product, through='CartItem')
    last_interact = models.DateTimeField(auto_now_add=datetime.now())


@receiver(pre_save, sender=Cart)
def generate_cart_hash(sender, instance, **kwargs):
    if not instance.hash_code:
        instance.hash_code = generate_unique_hash()


class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(validators=[MinValueValidator(1)])
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='cart_items')

    def __str__(self):
        return f'cart:{self.cart.id} - {self.product} - {self.quantity} pcs'


class FeaturedProducts(models.Model):
    hash_code = models.CharField(max_length=64, unique=True)
    products = models.ManyToManyField(Product, through='FeaturedItem')
    last_interact = models.DateTimeField(auto_now_add=datetime.now())


@receiver(pre_save, sender=FeaturedProducts)
def generate_featured_hash(sender, instance, **kwargs):
    if not instance.hash_code:
        instance.hash_code = generate_unique_hash()


class FeaturedItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    featured_products = models.ForeignKey(FeaturedProducts, on_delete=models.CASCADE, related_name='featured_items')

    def __str__(self):
        return f'featured:{self.featured_products} - {self.product}'
