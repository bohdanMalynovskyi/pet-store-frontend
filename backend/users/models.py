import binascii
import hashlib
import os
import random
from datetime import datetime

from django.contrib.auth.base_user import BaseUserManager
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator
from django.db import models
from django.db.models.signals import post_save, pre_save, post_delete, pre_delete
from django.dispatch import receiver
from pytz import timezone

from products.models import Product, ChangeablePrice
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
    # counterparty_ref = models.CharField(max_length=36, blank=True, null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'second_name', 'last_name', 'phone_number']
    objects = UserManager()


def generate_unique_hash():
    hash_code = hashlib.sha256(str(random.getrandbits(256)).encode('utf-8')).hexdigest()
    return hash_code


class HashCode(models.Model):
    key = models.CharField(_("Key"), max_length=40, primary_key=True)

    def save(self, *args, **kwargs):
        if not self.key:
            self.key = self.generate_key()
        return super().save(*args, **kwargs)

    @classmethod
    def generate_key(cls):
        return binascii.hexlify(os.urandom(20)).decode()

    def __str__(self):
        return self.key


class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True, related_name='cart')
    hash_code = models.OneToOneField(HashCode, on_delete=models.CASCADE, null=True, blank=True)
    products = models.ManyToManyField(Product, through='CartItem')
    last_interact = models.DateTimeField(auto_now_add=datetime.now(kiev_tz))

    def delete(self, using=None, keep_parents=False):
        self.hash_code.delete()

    def __str__(self):
        return f'cart {self.id} - {self.user}'


class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(
        validators=[MinValueValidator(1, 'Quantity must be greater than or equal to 1.')])
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='cart_items')
    changeable_price = models.ForeignKey(ChangeablePrice, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f'cart:{self.cart.id} - {self.product} - {self.quantity} pcs'

    def save(self, *args, **kwargs):
        if self.changeable_price:
            if self.product != self.changeable_price.product:
                raise ValidationError('Changeable price must belong to product')
        super().save()


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
    changeable_price = models.ForeignKey(ChangeablePrice, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f'featured:{self.featured_products} - {self.product}'

    def save(self, *args, **kwargs):
        if self.changeable_price:
            if self.product != self.changeable_price.product:
                raise ValidationError('Changeable price must belong to product')
        super().save()


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
