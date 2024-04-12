# Generated by Django 5.0.1 on 2024-04-11 19:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_cartitem_changeable_price_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='contact_person_ref',
            field=models.CharField(blank=True, max_length=36, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='counterparty_ref',
            field=models.CharField(blank=True, max_length=36, null=True),
        ),
        migrations.AlterField(
            model_name='cart',
            name='hash_code',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cart', to='users.hashcode'),
        ),
        migrations.AlterField(
            model_name='featuredproducts',
            name='hash_code',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='featured', to='users.hashcode'),
        ),
    ]
