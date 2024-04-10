from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator
from django.db import models

from products.models import Product, ChangeablePrice
from users.models import User, UnregisteredUser


class Order(models.Model):
    STATUS = (
        ('in_process', 'В обробці'),
        ('waiting_for_payment', 'Очікує оплати'),
        ('payed', 'Оплачено'),
        ('waiting_for_sending', 'Готується до відправки'),
        ('sent', 'Відправлено'),
        ('received', 'Отримано'),
        ('cancelled', 'Скасовано'),
        ('returned', 'Повернено')
    )
    PAYMENT_TYPE = (
        ('cash', 'Накладений платіж'),
        ('online', 'Онлайн-оплата'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name='orders')
    unregistered_user = models.ForeignKey(UnregisteredUser, on_delete=models.CASCADE, null=True, blank=True,
                                          related_name='orders')
    ref = models.CharField(max_length=36, null=True, blank=True)
    products = models.ManyToManyField(Product, through='OrderItem')
    status = models.CharField(choices=STATUS, max_length=22, null=False, blank=False)
    payment_type = models.CharField(choices=PAYMENT_TYPE, max_length=7, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    finished_at = models.DateTimeField(null=True, blank=True)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return f'order {self.id} - {self.user} - {self.get_status_display()}'

    def save(self, *args, **kwargs):
        if self.status not in dict(self.STATUS).keys():
            raise ValidationError(f"Order status must be one of: {', '.join(dict(self.STATUS).keys())}")

        if self.payment_type not in dict(self.PAYMENT_TYPE).keys():
            raise ValidationError(f"Payment type must be one of: {', '.join(dict(self.PAYMENT_TYPE).keys())}")
        super().save()


class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    fixed_price = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
    quantity = models.PositiveIntegerField(
        validators=[MinValueValidator(1, 'Quantity must be greater than or equal to 1.')])
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order_items')
    changeable_price = models.ForeignKey(ChangeablePrice, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f'Order:{self.order.id} - {self.product} - {self.quantity} pcs'
