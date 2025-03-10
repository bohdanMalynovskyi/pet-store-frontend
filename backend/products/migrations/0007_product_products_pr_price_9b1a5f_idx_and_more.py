# Generated by Django 5.0.1 on 2024-11-28 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0003_animalcategory_key_productcategory_key_and_more'),
        ('products', '0006_alter_product_weight'),
    ]

    operations = [
        migrations.AddIndex(
            model_name='product',
            index=models.Index(fields=['price'], name='products_pr_price_9b1a5f_idx'),
        ),
        migrations.AddIndex(
            model_name='product',
            index=models.Index(fields=['discount'], name='products_pr_discoun_0fa1d1_idx'),
        ),
        migrations.AddIndex(
            model_name='product',
            index=models.Index(fields=['subcategory'], name='products_pr_subcate_f595a1_idx'),
        ),
        migrations.AddIndex(
            model_name='product',
            index=models.Index(fields=['is_new'], name='products_pr_is_new_ab0139_idx'),
        ),
    ]
