from django.db import migrations


def insert_initial_data(apps, schema_editor):
    AnimalCategory = apps.get_model('categories', 'AnimalCategory')
    ProductCategory = apps.get_model('categories', 'ProductCategory')
    SubCategory = apps.get_model('categories', 'SubCategory')

    # Вставка данных в AnimalCategory
    AnimalCategory.objects.create(name='Собакам', key='dogs')
    AnimalCategory.objects.create(name='Котам', key='cats')
    AnimalCategory.objects.create(name='Гризунам', key='rodents')
    AnimalCategory.objects.create(name='Птахам', key='birds')
    AnimalCategory.objects.create(name='Рибам', key='fish')
    AnimalCategory.objects.create(name='Рептиліям', key='reptiles')

    # Вставка данных в ProductCategory
    product_category1 = ProductCategory.objects.create(name='Харчування', animal_category_id=1, key='feed')
    product_category2 = ProductCategory.objects.create(name='Харчування', animal_category_id=2, key='feed')
    product_category3 = ProductCategory.objects.create(name='Харчування', animal_category_id=3, key='feed')
    product_category4 = ProductCategory.objects.create(name='Харчування', animal_category_id=4, key='feed')
    product_category5 = ProductCategory.objects.create(name='Харчування', animal_category_id=5, key='feed')
    product_category6 = ProductCategory.objects.create(name='Харчування', animal_category_id=6, key='feed')

    product_category7 = ProductCategory.objects.create(name='Догляд і гігієна', animal_category_id=1, key='hygiene')
    product_category8 = ProductCategory.objects.create(name='Догляд і гігієна', animal_category_id=2, key='hygiene')
    product_category9 = ProductCategory.objects.create(name='Догляд і гігієна', animal_category_id=3, key='hygiene')
    product_category10 = ProductCategory.objects.create(name='Догляд і гігієна', animal_category_id=4, key='hygiene')
    product_category11 = ProductCategory.objects.create(name='Догляд і гігієна', animal_category_id=5, key='hygiene')
    product_category12 = ProductCategory.objects.create(name='Догляд і гігієна', animal_category_id=6, key='hygiene')

    product_category13 = ProductCategory.objects.create(name="Здоров'я", animal_category_id=1, key='healthcare')
    product_category14 = ProductCategory.objects.create(name="Здоров'я", animal_category_id=2, key='healthcare')
    product_category15 = ProductCategory.objects.create(name="Здоров'я", animal_category_id=3, key='healthcare')
    product_category16 = ProductCategory.objects.create(name="Здоров'я", animal_category_id=4, key='healthcare')
    product_category17 = ProductCategory.objects.create(name="Здоров'я", animal_category_id=5, key='healthcare')
    product_category18 = ProductCategory.objects.create(name="Здоров'я", animal_category_id=6, key='healthcare')

    product_category19 = ProductCategory.objects.create(name="Аксесуари", animal_category_id=1, key='accessories')
    product_category20 = ProductCategory.objects.create(name="Аксесуари", animal_category_id=2, key='accessories')
    product_category21 = ProductCategory.objects.create(name="Аксесуари", animal_category_id=3, key='accessories')
    product_category22 = ProductCategory.objects.create(name="Аксесуари", animal_category_id=4, key='accessories')
    product_category23 = ProductCategory.objects.create(name="Аксесуари", animal_category_id=5, key='accessories')
    product_category24 = ProductCategory.objects.create(name="Аксесуари", animal_category_id=6, key='accessories')

    # Вставка данных в SubCategory
    SubCategory.objects.create(name='Сухий корм', product_category=product_category1, key='dry-feed')
    SubCategory.objects.create(name='Вологий корм', product_category=product_category1, key='wet-feed')
    SubCategory.objects.create(name='Лікувальний корм', product_category=product_category1, key='med-feed')
    SubCategory.objects.create(name='Ласощі для собак', product_category=product_category1, key='dog-treats')

    SubCategory.objects.create(name='Сухий корм', product_category=product_category2, key='dry-feed')
    SubCategory.objects.create(name='Вологий корм', product_category=product_category2, key='wet-feed')
    SubCategory.objects.create(name='Лікувальний корм', product_category=product_category2, key='med-feed')
    SubCategory.objects.create(name='Ласощі для котів', product_category=product_category2, key='cat-treats')

    SubCategory.objects.create(name='Корм для гризунів', product_category=product_category3, key='rodents-feed')
    SubCategory.objects.create(name='Ласощі для гризунів', product_category=product_category3, key='rodents-treats')

    SubCategory.objects.create(name='Корм для птахів', product_category=product_category4, key='birds-feed')
    SubCategory.objects.create(name='Ласощі для птахів', product_category=product_category4, key='birds-treats')

    SubCategory.objects.create(name='Корм для риб', product_category=product_category5, key='fish-feed')

    SubCategory.objects.create(name='Корм для рептилій', product_category=product_category6, key='reptiles-feed')

    SubCategory.objects.create(name='Інструменти для догляду', product_category=product_category7, key='care-tools')
    SubCategory.objects.create(name='Косметика для собак', product_category=product_category7, key='dogs-cosmetics')
    SubCategory.objects.create(name='Засоби для прибирання в домі', product_category=product_category7,
                               key='clean-products')

    SubCategory.objects.create(name='Інструменти для догляду', product_category=product_category8, key='care-tools')
    SubCategory.objects.create(name='Косметика для котів', product_category=product_category8, key='cats-cosmetics')
    SubCategory.objects.create(name='Засоби для прибирання в домі', product_category=product_category8,
                               key='clean-products')

    SubCategory.objects.create(name='Засоби догляду та гігієни для гризунів', product_category=product_category9,
                               key='rodents-care')
    SubCategory.objects.create(name='Засоби для прибирання в домі', product_category=product_category9,
                               key='clean-products')

    SubCategory.objects.create(name='Засоби догляду', product_category=product_category10, key='care-tools')
    SubCategory.objects.create(name='Засоби для прибирання в домі', product_category=product_category10,
                               key='clean-products')
    SubCategory.objects.create(name='Купалки для птахів', product_category=product_category10, key='bird-bath')

    SubCategory.objects.create(name='Догляд за водою і рослинами', product_category=product_category11, key='env-care')

    SubCategory.objects.create(name='Засоби догляду за рептиліями', product_category=product_category12,
                               key='reptiles-care')

    SubCategory.objects.create(name='Засоби від паразитів', product_category=product_category13, key='anti-parasites')
    SubCategory.objects.create(name='Вітаміни', product_category=product_category13, key='vitamins')
    SubCategory.objects.create(name='Харчові добавки', product_category=product_category13, key='nutritional-supplies')

    SubCategory.objects.create(name='Засоби від паразитів', product_category=product_category14, key='anti-parasites')
    SubCategory.objects.create(name='Вітаміни', product_category=product_category14, key='vitamins')
    SubCategory.objects.create(name='Харчові добавки', product_category=product_category14, key='nutritional-supplies')

    SubCategory.objects.create(name='Засоби від паразитів', product_category=product_category15, key='anti-parasites')
    SubCategory.objects.create(name='Вітаміни', product_category=product_category15, key='vitamins')

    SubCategory.objects.create(name='Харчові добавки', product_category=product_category16, key='nutritional-supplies')
    SubCategory.objects.create(name='Вітаміни', product_category=product_category16, key='vitamins')

    SubCategory.objects.create(name='Вітаміни', product_category=product_category17, key='vitamins')

    SubCategory.objects.create(name='Харчові добавки', product_category=product_category18, key='nutritional-supplies')
    SubCategory.objects.create(name='Вітаміни', product_category=product_category18, key='vitamins')

    SubCategory.objects.create(name='Одяг', product_category=product_category19, key='clothing')
    SubCategory.objects.create(name='Сумки і переноски для собак', product_category=product_category19, key='carries')
    SubCategory.objects.create(name='Миски та поїлки для собак', product_category=product_category19, key='bowls')
    SubCategory.objects.create(name='Іграшки', product_category=product_category19, key='toys')
    SubCategory.objects.create(name='Туалети та пакети для збирання', product_category=product_category19,
                               key='toilets')
    SubCategory.objects.create(name='Будки, вольєри для собак', product_category=product_category19, key='cells')
    SubCategory.objects.create(name='Дресирування та спорт', product_category=product_category19, key='sports')
    SubCategory.objects.create(name='Лежанки та спальні місця', product_category=product_category19, key='couches')
    SubCategory.objects.create(name='Амуніція для собак', product_category=product_category19, key='dogs-equipments')

    SubCategory.objects.create(name='Одяг', product_category=product_category20, key='clothing')
    SubCategory.objects.create(name='Сумки і переноски для котів', product_category=product_category20, key='carries')
    SubCategory.objects.create(name='Миски та поїлки для котів', product_category=product_category20, key='bowls')
    SubCategory.objects.create(name='Туалети та наповнювачі', product_category=product_category20, key='toilets')
    SubCategory.objects.create(name='Іграшки', product_category=product_category20, key='toys')
    SubCategory.objects.create(name='Кігтеточки', product_category=product_category20, key='claw-sharpener')
    SubCategory.objects.create(name='Спальні місця', product_category=product_category20, key='couches')

    SubCategory.objects.create(name='Клітки, вольєри для гризунів', product_category=product_category21, key='cells')
    SubCategory.objects.create(name='Переноски', product_category=product_category21, key='carries')
    SubCategory.objects.create(name='Годівниці для гризунів', product_category=product_category21, key='bowls')
    SubCategory.objects.create(name='Туалети, підстилки для гризунів', product_category=product_category21,
                               key='toilets')
    SubCategory.objects.create(name='Іграшки', product_category=product_category21, key='toys')

    SubCategory.objects.create(name='Клітки, вольєри, переноски', product_category=product_category22, key='cells')
    SubCategory.objects.create(name='Наповнювачі, підстилки', product_category=product_category22, key='fillers')
    SubCategory.objects.create(name='Годівниці', product_category=product_category22, key='bowls')
    SubCategory.objects.create(name='Іграшки для птахів', product_category=product_category22, key='toys')

    SubCategory.objects.create(name='Акваріум для риб', product_category=product_category23, key='aquarium')
    SubCategory.objects.create(name='Устаткування для акваріумів', product_category=product_category23,
                               key='aqua-equipments')
    SubCategory.objects.create(name='Годівниці для риб', product_category=product_category23, key='bowls')
    SubCategory.objects.create(name='Хімія для акваріума', product_category=product_category23, key='aqua-care')

    SubCategory.objects.create(name='Тераріум', product_category=product_category24, key='terrarium')
    SubCategory.objects.create(name='Устаткування для тераріумів', product_category=product_category24,
                               key='terra-equipments')
    SubCategory.objects.create(name='Субстрати, підстилки для тераріумів', product_category=product_category24,
                               key='fillers')


class Migration(migrations.Migration):
    dependencies = [
        ('categories', '0003_animalcategory_key_productcategory_key_and_more'),  # Зависимость от предыдущей миграции
    ]

    operations = [
        migrations.RunPython(insert_initial_data),
    ]
