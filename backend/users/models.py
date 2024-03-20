import hashlib
import random
from datetime import datetime

from django.contrib.auth.base_user import BaseUserManager
from django.core.validators import MinValueValidator
from django.db import models
from django.db.models.signals import post_save, pre_save, post_delete, pre_delete
from django.dispatch import receiver
from pytz import timezone

from products.models import Product
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from rest_framework.authtoken.models import Token

kiev_tz = timezone('Europe/Kiev')


class UserManager(BaseUserManager):
    """Define a model manager for User model with no username field."""

    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """Create and save a User with the given email and password."""
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        """Create and save a regular User with the given email and password."""
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        """Create and save a SuperUser with the given email and password."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)


class User(AbstractUser):
    """User model."""

    username = None
    email = models.EmailField(_('email address'), unique=True, blank=False, null=False)
    second_name = models.CharField(max_length=150, blank=True)
    phone_number = models.CharField(max_length=15, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'second_name', 'last_name', 'phone_number']
    objects = UserManager()


def generate_unique_hash():
    hash_code = hashlib.sha256(str(random.getrandbits(256)).encode('utf-8')).hexdigest()
    return hash_code


class HashCode(models.Model):
    token = models.CharField(max_length=64, null=False, blank=False, db_index=True)


class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True, related_name='cart')
    hash_code = models.OneToOneField(HashCode, on_delete=models.CASCADE, null=True, blank=True)
    products = models.ManyToManyField(Product, through='CartItem')
    last_interact = models.DateTimeField(auto_now_add=datetime.now(kiev_tz))

    def delete(self, using=None, keep_parents=False):
        self.hash_code.delete()


class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(validators=[MinValueValidator(1)])
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='cart_items')

    def __str__(self):
        return f'cart:{self.cart.id} - {self.product} - {self.quantity} pcs'


class FeaturedProducts(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True, related_name='featured')
    hash_code = models.OneToOneField(HashCode, on_delete=models.CASCADE, null=True, blank=True)
    products = models.ManyToManyField(Product, through='FeaturedItem')
    last_interact = models.DateTimeField(auto_now_add=datetime.now(kiev_tz))

    def delete(self, using=None, keep_parents=False):
        self.hash_code.delete()


class FeaturedItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    featured_products = models.ForeignKey(FeaturedProducts, on_delete=models.CASCADE, related_name='featured_items')

    def __str__(self):
        return f'featured:{self.featured_products} - {self.product}'


@receiver(pre_save, sender=HashCode)
def generate_cart_hash(sender, instance, **kwargs):
    if not instance.token:
        instance.token = generate_unique_hash()


@receiver(pre_save, sender=Cart)
def generate_cart_hash(sender, instance, **kwargs):
    if not instance.hash_code and not instance.user:
        hash_code = HashCode.objects.create()
        instance.hash_code = hash_code


@receiver(pre_save, sender=FeaturedProducts)
def generate_featured_hash(sender, instance, **kwargs):
    if not instance.hash_code and not instance.user:
        hash_code = HashCode.objects.create()
        instance.hash_code = hash_code
