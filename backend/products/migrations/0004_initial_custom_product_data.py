from django.db import migrations, models
from django.core.validators import MinValueValidator, MaxValueValidator


def create_initial_data(apps, schema_editor):
    Product = apps.get_model('products', 'Product')
    Brand = apps.get_model('products', 'Brand')
    ChangeablePrice = apps.get_model('products', 'ChangeablePrice')
    ProductImages = apps.get_model('products', 'ProductImages')
    AdditionalFields = apps.get_model('products', 'AdditionalFields')
    SubCategory = apps.get_model('categories', 'SubCategory')

    # Create three instances of Brand
    Brand.objects.bulk_create([
        Brand(name='Brand1', country='Country1'),
        Brand(name='Brand2', country='Country2'),
        Brand(name='Brand3', country='Country3'),
    ])

    # Create three instances of Product
    Product.objects.bulk_create([
        Product(name='Product1', price=10.00, discount=20, weight=1, brand=Brand.objects.get(name='Brand2'),
                subcategory=SubCategory.objects.all().first(), description='Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi finibus, nunc in cursus pretium, nibh mi egestas nunc, eget volutpat leo libero eget lectus. Proin venenatis accumsan leo, nec facilisis est faucibus rhoncus. Donec vitae ipsum augue. Vestibulum eleifend, magna euismod condimentum molestie, dolor arcu fringilla est, sed tincidunt sapien neque et urna. Vestibulum at vehicula lorem, volutpat finibus ex. Donec malesuada id mauris vitae iaculis. Etiam eget mi metus.'),
        Product(name='Product2', brand=Brand.objects.get(name='Brand3'),
                subcategory=SubCategory.objects.all()[1], price=5, discount=2, weight=0.5),
        Product(name='Product3', price=30.00, weight=2, brand=Brand.objects.get(name='Brand1'),
                subcategory=SubCategory.objects.all().last()),
        Product(name='Product4', price=12.00, discount=10, weight=1, brand=Brand.objects.get(name='Brand2'),
                subcategory=SubCategory.objects.all().first()),
        Product(name='Product5', brand=Brand.objects.get(name='Brand3'),
                subcategory=SubCategory.objects.all()[2], price=24, discount=5, weight=0.5),
        Product(name='Product6', price=35.00, weight=2, brand=Brand.objects.get(name='Brand1'),
                subcategory=SubCategory.objects.all().last()),
        Product(name='Product7', brand=Brand.objects.get(name='Brand3'),
                subcategory=SubCategory.objects.all()[6], price=125, discount=25, weight=0.5),
        Product(name='Product8', brand=Brand.objects.get(name='Brand3'),
                subcategory=SubCategory.objects.all()[3], price=125, discount=25, weight=0.5),
        Product(name='Product9', price=45, weight=2, brand=Brand.objects.get(name='Brand1'),
                subcategory=SubCategory.objects.all().last()),
        Product(name='Product10', price=45, weight=2, brand=Brand.objects.get(name='Brand1'),
                subcategory=SubCategory.objects.all().last())
    ])

    # Create three instances of ChangeablePrice
    ChangeablePrice.objects.bulk_create([
        ChangeablePrice(product=Product.objects.get(name='Product2'), price=5.00, discount=2, order=1, size='S'),
        ChangeablePrice(product=Product.objects.get(name='Product2'), price=15.00, discount=2, order=2, size='M'),
        ChangeablePrice(product=Product.objects.get(name='Product2'), price=25.00, discount=2, order=3, size='L'),
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
        ProductImages(product=Product.objects.get(name='Product4'), image='images-to-upload/0000068831.jpg',
                      order=1),
        ProductImages(product=Product.objects.get(name='Product5'), image='images-to-upload/0000068831.jpg',
                      order=1),
        ProductImages(product=Product.objects.get(name='Product6'), image='images-to-upload/0000068831.jpg',
                      order=1),
        ProductImages(product=Product.objects.get(name='Product7'), image='images-to-upload/0000068831.jpg',
                      order=1),
        ProductImages(product=Product.objects.get(name='Product8'), image='images-to-upload/0000068831.jpg',
                      order=1),
        ProductImages(product=Product.objects.get(name='Product9'), image='images-to-upload/0000068831.jpg',
                      order=1)
    ])

    text = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi finibus, nunc in cursus pretium, nibh mi egestas nunc, eget volutpat leo libero eget lectus.'
    # Create three instances of Additional Fields
    AdditionalFields.objects.bulk_create([
        AdditionalFields(product=Product.objects.get(name='Product1'), title='Tag1', text=text),
        AdditionalFields(product=Product.objects.get(name='Product1'), title='Tag2', text=text),
        AdditionalFields(product=Product.objects.get(name='Product1'), title='Tag3', text=text),
        AdditionalFields(product=Product.objects.get(name='Product1'), title='Tag4', text=text),
    ])


class Migration(migrations.Migration):
    dependencies = [
        ('products', '0003_search_conf'),
    ]

    operations = [
        migrations.RunPython(create_initial_data),
    ]
