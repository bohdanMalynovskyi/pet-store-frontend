from django.urls import path, include
from rest_framework.routers import SimpleRouter

from users import views

router = SimpleRouter()

urlpatterns = [
    path('cart/create/', views.create_cart, name='create-cart'),
    path('cart/<int:cart_pk>/', views.get_cart, name='get-cart'),
    path('cart/<int:cart_pk>/add/<int:product_pk>/', views.add_to_cart, name='add-to-cart'),
    path('cart/<int:cart_pk>/decrease/<int:product_pk>/', views.decrease_quantity, name='decrease-quantity'),
    path('cart/<int:cart_pk>/delete/<int:product_pk>/', views.delete_cart_item, name='delete-cart-item'),
    path('cart/<int:cart_pk>/clear/', views.clear_cart, name='clear-cart'),

    path('featured/create/', views.create_featured_products, name='create-featured'),
    path('featured/<int:featured_pk>/', views.get_featured, name='get-featured'),
    path('featured/<int:featured_pk>/add/<int:product_pk>/', views.add_to_featured, name='add-to-featured'),
    path('featured/<int:featured_pk>/delete/<int:product_pk>/', views.delete_featured_item, name='delete-featured-item'),
    path('featured/<int:featured_pk>/clear/', views.clear_featured, name='clear-featured'),
]

urlpatterns += router.urls
