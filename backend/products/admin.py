from django.contrib import admin

from products.models import ProductImages, ChangeablePrice, Product, Brand, Tags

admin.site.register(Brand)
admin.site.register(Product)
admin.site.register(ChangeablePrice)
admin.site.register(ProductImages)
admin.site.register(Tags)
