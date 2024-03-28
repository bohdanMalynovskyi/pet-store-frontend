from django.urls import path, include
from rest_framework.routers import SimpleRouter

from users import views

router = SimpleRouter()

urlpatterns = [
    path('cart/create/', views.create_cart, name='create-cart'),
    path('cart/', views.get_cart, name='get-cart'),
    path('cart/add/<int:product_pk>/', views.add_to_cart, name='add-to-cart'),
    path('cart/product/<int:product_pk>/changeable_price/<int:changeable_price_pk>/',
         views.change_cart_item_changeable_price, name='change-cart-changeable-price'),
    path('cart/decrease/<int:product_pk>/', views.decrease_quantity, name='decrease-quantity'),
    path('cart/delete/<int:product_pk>/', views.delete_cart_item, name='delete-cart-item'),
    path('cart/clear/', views.clear_cart, name='clear-cart'),

    path('featured/create/', views.create_featured_products, name='create-featured'),
    path('featured/', views.get_featured, name='get-featured'),
    path('featured/add/<int:product_pk>/', views.add_to_featured, name='add-to-featured'),
    path('featured/product/<int:product_pk>/changeable_price/<int:changeable_price_pk>/',
         views.change_cart_item_changeable_price, name='change-featured-changeable-price'),
    path('featured/delete/<int:product_pk>/', views.delete_featured_item, name='delete-featured-item'),
    path('featured/clear/', views.clear_featured, name='clear-featured'),
]

urlpatterns += router.urls
