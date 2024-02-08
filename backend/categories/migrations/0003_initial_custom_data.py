from django.db import migrations


def insert_initial_data(apps, schema_editor):
    AnimalCategory = apps.get_model('categories', 'AnimalCategory')
    ProductCategory = apps.get_model('categories', 'ProductCategory')
    SubCategory = apps.get_model('categories', 'SubCategory')

    # Вставка данных в AnimalCategory
    AnimalCategory.objects.create(name='Dogs')
    AnimalCategory.objects.create(name='Cats')
    AnimalCategory.objects.create(name='Parrots')

    # Вставка данных в ProductCategory
    product_category1 = ProductCategory.objects.create(name='Food', animal_category_id=1)
    product_category2 = ProductCategory.objects.create(name='Toy', animal_category_id=1)
    product_category3 = ProductCategory.objects.create(name='Toy', animal_category_id=2)

    # Вставка данных в SubCategory
    SubCategory.objects.create(name='Wet food', product_category=product_category1)
    SubCategory.objects.create(name='Dry food', product_category=product_category1)
    SubCategory.objects.create(name='Soft toy', product_category=product_category3)


class Migration(migrations.Migration):
    dependencies = [
        ('categories', '0002_alter_animalcategory_options_and_more'),  # Зависимость от предыдущей миграции
    ]

    operations = [
        migrations.RunPython(insert_initial_data),
    ]
