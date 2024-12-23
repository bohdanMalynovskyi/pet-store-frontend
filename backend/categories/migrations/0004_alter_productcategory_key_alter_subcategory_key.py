# Generated by Django 5.0.1 on 2024-12-23 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0003_animalcategory_key_productcategory_key_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productcategory',
            name='key',
            field=models.CharField(default='', max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='subcategory',
            name='key',
            field=models.CharField(default='', max_length=100, unique=True),
        ),
    ]