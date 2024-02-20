from django.contrib import admin

from users.models import Cart, CartItem, FeaturedProducts, FeaturedItem

admin.site.register(Cart)
admin.site.register(CartItem)
admin.site.register(FeaturedProducts)
admin.site.register(FeaturedItem)
