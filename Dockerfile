FROM postgres:16

COPY postgres_uk_locale/uk_UA.affix /usr/share/postgresql/16/tsearch_data/uk_ua.affix
COPY postgres_uk_locale/uk_UA.dict /usr/share/postgresql/16/tsearch_data/uk_ua.dict
COPY postgres_uk_locale/ukrainian.stop /usr/share/postgresql/16/tsearch_data/ukrainian.stop
