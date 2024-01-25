from django.contrib import admin

from categories.models import AnimalCategory, SubCategory, ProductCategory

admin.site.register(AnimalCategory)
admin.site.register(ProductCategory)
admin.site.register(SubCategory)
