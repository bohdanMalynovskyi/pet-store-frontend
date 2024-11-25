from django.contrib.postgres.search import SearchVector
from django.db import migrations


def compute_search_vector(apps, schema_editor):
    Product = apps.get_model("products", "Product")
    Product.objects.update(search_vector=SearchVector('name', 'description', config='ukrainian'))


class Migration(migrations.Migration):
    dependencies = [
        ('products', '0004_product_search_vector_and_more'),
    ]

    operations = [
        migrations.RunSQL(
            sql="""
            CREATE TRIGGER product_search_vector_update BEFORE INSERT OR UPDATE
            ON products_product
            FOR EACH ROW EXECUTE FUNCTION
            tsvector_update_trigger(search_vector, 'public.ukrainian', 'name', 'description');
            """,
            reverse_sql="""
            DROP TRIGGER IF EXISTS product_search_vector_update ON products_product;
            """
        ),
        migrations.RunPython(compute_search_vector),
    ]
