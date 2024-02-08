from django.db import migrations


def insert_initial_data(apps, schema_editor):
    AnimalCategory = apps.get_model('categories', 'AnimalCategory')
    ProductCategory = apps.get_model('categories', 'ProductCategory')
    SubCategory = apps.get_model('categories', 'SubCategory')

    # Вставка данных в AnimalCategory
    AnimalCategory.objects.create(name='Собакам')
    AnimalCategory.objects.create(name='Котам')
    AnimalCategory.objects.create(name='Гризунам')
    AnimalCategory.objects.create(name='Птахам')
    AnimalCategory.objects.create(name='Рибам')
    AnimalCategory.objects.create(name='Рептиліям')

    # Вставка данных в ProductCategory
    product_category1 = ProductCategory.objects.create(name='Харчування', animal_category_id=1)
    product_category2 = ProductCategory.objects.create(name='Харчування', animal_category_id=2)
    product_category3 = ProductCategory.objects.create(name='Харчування', animal_category_id=3)
    product_category4 = ProductCategory.objects.create(name='Харчування', animal_category_id=4)
    product_category5 = ProductCategory.objects.create(name='Харчування', animal_category_id=5)
    product_category6 = ProductCategory.objects.create(name='Харчування', animal_category_id=6)

    product_category7 = ProductCategory.objects.create(name='Догляд і гігієна', animal_category_id=1)
    product_category8 = ProductCategory.objects.create(name='Догляд і гігієна', animal_category_id=2)
    product_category9 = ProductCategory.objects.create(name='Догляд і гігієна', animal_category_id=3)
    product_category10 = ProductCategory.objects.create(name='Догляд і гігієна', animal_category_id=4)
    product_category11 = ProductCategory.objects.create(name='Догляд і гігієна', animal_category_id=5)
    product_category12 = ProductCategory.objects.create(name='Догляд і гігієна', animal_category_id=6)

    product_category13 = ProductCategory.objects.create(name="Здоров'я", animal_category_id=1)
    product_category14 = ProductCategory.objects.create(name="Здоров'я", animal_category_id=2)
    product_category15 = ProductCategory.objects.create(name="Здоров'я", animal_category_id=3)
    product_category16 = ProductCategory.objects.create(name="Здоров'я", animal_category_id=4)
    product_category17 = ProductCategory.objects.create(name="Здоров'я", animal_category_id=5)
    product_category18 = ProductCategory.objects.create(name="Здоров'я", animal_category_id=6)

    product_category19 = ProductCategory.objects.create(name="Аксесуари", animal_category_id=1)
    product_category20 = ProductCategory.objects.create(name="Аксесуари", animal_category_id=2)
    product_category21 = ProductCategory.objects.create(name="Аксесуари", animal_category_id=3)
    product_category22 = ProductCategory.objects.create(name="Аксесуари", animal_category_id=4)
    product_category23 = ProductCategory.objects.create(name="Аксесуари", animal_category_id=5)
    product_category24 = ProductCategory.objects.create(name="Аксесуари", animal_category_id=6)

    # Вставка данных в SubCategory
    SubCategory.objects.create(name='Сухий корм', product_category=product_category1)
    SubCategory.objects.create(name='Вологий корм', product_category=product_category1)
    SubCategory.objects.create(name='Лікувальний корм', product_category=product_category1)
    SubCategory.objects.create(name='Ласощі для собак', product_category=product_category1)

    SubCategory.objects.create(name='Сухий корм', product_category=product_category2)
    SubCategory.objects.create(name='Вологий корм', product_category=product_category2)
    SubCategory.objects.create(name='Лікувальний корм', product_category=product_category2)
    SubCategory.objects.create(name='Ласощі для котів', product_category=product_category2)

    SubCategory.objects.create(name='Сухий корм', product_category=product_category2)
    SubCategory.objects.create(name='Вологий корм', product_category=product_category2)
    SubCategory.objects.create(name='Лікувальний корм', product_category=product_category2)
    SubCategory.objects.create(name='Ласощі для котів', product_category=product_category2)

    SubCategory.objects.create(name='Корм для гризунів', product_category=product_category3)
    SubCategory.objects.create(name='Ласощі для гризунів', product_category=product_category3)

    SubCategory.objects.create(name='Корм для птахів', product_category=product_category4)
    SubCategory.objects.create(name='Ласощі для птахів', product_category=product_category4)

    SubCategory.objects.create(name='Корм для риб', product_category=product_category5)

    SubCategory.objects.create(name='Корм для рептилій', product_category=product_category6)

    SubCategory.objects.create(name='Інструменти для догляду', product_category=product_category7)
    SubCategory.objects.create(name='Косметика для собак', product_category=product_category7)
    SubCategory.objects.create(name='Засоби для прибирання в домі', product_category=product_category7)

    SubCategory.objects.create(name='Інструменти для догляду', product_category=product_category8)
    SubCategory.objects.create(name='Косметика для котів', product_category=product_category8)
    SubCategory.objects.create(name='Засоби для прибирання в домі', product_category=product_category8)

    SubCategory.objects.create(name='Засоби догляду та гігієни для гризунів', product_category=product_category9)
    SubCategory.objects.create(name='Засоби для прибирання в домі', product_category=product_category9)

    SubCategory.objects.create(name='Засоби догляду', product_category=product_category10)
    SubCategory.objects.create(name='Засоби для прибирання в домі', product_category=product_category10)
    SubCategory.objects.create(name='Купалки для птахів', product_category=product_category10)

    SubCategory.objects.create(name='Догляд за водою і рослинами', product_category=product_category11)

    SubCategory.objects.create(name='Засоби догляду за рептиліями', product_category=product_category12)

    SubCategory.objects.create(name='Засоби від паразитів', product_category=product_category13)
    SubCategory.objects.create(name='Вітаміни', product_category=product_category13)
    SubCategory.objects.create(name='Харчові добавки', product_category=product_category13)

    SubCategory.objects.create(name='Засоби від паразитів', product_category=product_category14)
    SubCategory.objects.create(name='Вітаміни', product_category=product_category14)
    SubCategory.objects.create(name='Харчові добавки', product_category=product_category14)

    SubCategory.objects.create(name='Засоби від паразитів', product_category=product_category15)
    SubCategory.objects.create(name='Вітаміни', product_category=product_category15)

    SubCategory.objects.create(name='Харчові добавки', product_category=product_category16)
    SubCategory.objects.create(name='Вітаміни', product_category=product_category16)

    SubCategory.objects.create(name='Вітаміни', product_category=product_category17)

    SubCategory.objects.create(name='Харчові добавки', product_category=product_category18)
    SubCategory.objects.create(name='Вітаміни', product_category=product_category18)



    SubCategory.objects.create(name='Одяг', product_category=product_category19)
    SubCategory.objects.create(name='Сумки і переноски для собак', product_category=product_category19)
    SubCategory.objects.create(name='Миски та поїлки для собак', product_category=product_category19)
    SubCategory.objects.create(name='Іграшки', product_category=product_category19)
    SubCategory.objects.create(name='Туалети та пакети для збирання', product_category=product_category19)
    SubCategory.objects.create(name='Будки, вольєри для собак', product_category=product_category19)
    SubCategory.objects.create(name='Дресирування та спорт', product_category=product_category19)
    SubCategory.objects.create(name='Лежанки та спальні місця', product_category=product_category19)
    SubCategory.objects.create(name='Амуніція для собак', product_category=product_category19)

    SubCategory.objects.create(name='Одяг', product_category=product_category20)
    SubCategory.objects.create(name='Сумки і переноски для котів', product_category=product_category20)
    SubCategory.objects.create(name='Миски та поїлки для котів', product_category=product_category20)
    SubCategory.objects.create(name='Туалети та наповнювачі', product_category=product_category20)
    SubCategory.objects.create(name='Іграшки', product_category=product_category20)
    SubCategory.objects.create(name='Кігтеточки', product_category=product_category20)
    SubCategory.objects.create(name='Спальні місця', product_category=product_category20)

    SubCategory.objects.create(name='Клітки, вольєри для гризунів', product_category=product_category21)
    SubCategory.objects.create(name='Переноски', product_category=product_category21)
    SubCategory.objects.create(name='Годівниці для гризунів', product_category=product_category21)
    SubCategory.objects.create(name='Туалети, підстилки для гризунів', product_category=product_category21)
    SubCategory.objects.create(name='Іграшки', product_category=product_category21)

    SubCategory.objects.create(name='Клітки, вольєри, переноски для гризунів', product_category=product_category22)
    SubCategory.objects.create(name='Наповнювачі, підстилки', product_category=product_category22)
    SubCategory.objects.create(name='Годівниці для гризунів', product_category=product_category22)
    SubCategory.objects.create(name='Іграшки для птахів', product_category=product_category22)

    SubCategory.objects.create(name='Акваріум для риб', product_category=product_category22)
    SubCategory.objects.create(name='Устаткування для акваріумів', product_category=product_category22)
    SubCategory.objects.create(name='Годівниці для риб', product_category=product_category22)
    SubCategory.objects.create(name='Хімія для акваріума', product_category=product_category22)

    SubCategory.objects.create(name='Тераріум', product_category=product_category22)
    SubCategory.objects.create(name='Устаткування для тераріумів', product_category=product_category22)
    SubCategory.objects.create(name='Субстрати, підстилки для тераріумів', product_category=product_category22)


class Migration(migrations.Migration):
    dependencies = [
        ('categories', '0002_alter_animalcategory_options_and_more'),  # Зависимость от предыдущей миграции
    ]

    operations = [
        migrations.RunPython(insert_initial_data),
    ]
