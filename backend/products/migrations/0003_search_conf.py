from django.conf import settings
from django.db import migrations


db_name = settings.DATABASES['default']['NAME']


class Migration(migrations.Migration):
    dependencies = [
        ('products', '0002_rename_sale_changeableprice_discount_and_more'),
    ]

    operations = [
        migrations.RunSQL(
            f"""
            ALTER DATABASE {db_name} SET timezone TO 'Europe/Kiev';
            """
        ),
        migrations.RunSQL(
            """
            -- Ваша текущая SQL команда
            CREATE TEXT SEARCH DICTIONARY ukrainian_huns (TEMPLATE = ispell, DictFile = uk_ua, AffFile = uk_ua, StopWords = ukrainian);
            CREATE TEXT SEARCH DICTIONARY ukrainian_stem (template = simple, stopwords = ukrainian);
            CREATE TEXT SEARCH CONFIGURATION ukrainian (PARSER=default);
            ALTER TEXT SEARCH CONFIGURATION ukrainian ALTER MAPPING FOR hword, hword_part, word WITH ukrainian_huns, ukrainian_stem;
            ALTER TEXT SEARCH CONFIGURATION ukrainian ALTER MAPPING FOR int, uint, numhword, numword, hword_numpart, email, float, file, url, url_path, version, host, sfloat WITH simple;
            ALTER TEXT SEARCH CONFIGURATION ukrainian ALTER MAPPING FOR asciihword, asciiword, hword_asciipart WITH english_stem;
            CREATE EXTENSION IF NOT EXISTS pg_trgm;
            """,
            "DROP TEXT SEARCH DICTIONARY ukrainian_huns; DROP TEXT SEARCH DICTIONARY ukrainian_stem; DROP TEXT SEARCH CONFIGURATION ukrainian;"
        ),
    ]
