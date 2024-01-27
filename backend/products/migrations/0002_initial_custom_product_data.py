from django.db import migrations, models
from django.core.validators import MinValueValidator, MaxValueValidator


def create_initial_data(apps, schema_editor):
    Product = apps.get_model('products', 'Product')
    Brand = apps.get_model('products', 'Brand')
    ChangeablePrice = apps.get_model('products', 'ChangeablePrice')
    ProductImages = apps.get_model('products', 'ProductImages')
    Tags = apps.get_model('products', 'Tags')

    # Create three instances of Brand
    Brand.objects.bulk_create([
        Brand(name='Brand1', country='Country1'),
        Brand(name='Brand2', country='Country2'),
        Brand(name='Brand3', country='Country3'),
    ])

    # Create three instances of Product
    Product.objects.bulk_create([
        Product(name='Product1', price=10.00, sale=20, brand=Brand.objects.get(name='Brand2')),
        Product(name='Product2', brand=Brand.objects.get(name='Brand3')),
        Product(name='Product3', price=30.00, brand=Brand.objects.get(name='Brand1')),
    ])

    # Create three instances of ChangeablePrice
    ChangeablePrice.objects.bulk_create([
        ChangeablePrice(product=Product.objects.get(name='Product2'), price=5.00, sale=2, order=1, size='S'),
        ChangeablePrice(product=Product.objects.get(name='Product2'), price=15.00, sale=2, order=2, size='M'),
        ChangeablePrice(product=Product.objects.get(name='Product2'), price=25.00, sale=2, order=3, size='L'),
    ])

    # Create three instances of ProductImages
    ProductImages.objects.bulk_create([
        ProductImages(product=Product.objects.get(name='Product1'), image='images-to-upload/0000068831.jpg',
                      order=1),
        ProductImages(product=Product.objects.get(name='Product1'), image='images-to-upload/0000068832.jpg',
                      order=3),
        ProductImages(product=Product.objects.get(name='Product1'), image='images-to-upload/0000068837.jpg',
                      order=2),
        ProductImages(product=Product.objects.get(name='Product2'), image='images-to-upload/0000123324.jpg',
                      order=1),
        ProductImages(product=Product.objects.get(name='Product3'), image='images-to-upload/0000137171.jpg',
                      order=1),
    ])

    # Create three instances of Tags
    Tags.objects.bulk_create([
        Tags(product=Product.objects.get(name='Product3'), title='Tag1', text='Tag text 1'),
        Tags(product=Product.objects.get(name='Product3'), title='Tag2', text='Tag text 2'),
        Tags(product=Product.objects.get(name='Product1'), title='Tag3', text='Tag text 3'),
        Tags(product=Product.objects.get(name='Product2'), title='Tag3', text='Tag text 3'),
    ])


class Migration(migrations.Migration):
    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_initial_data),
    ]
