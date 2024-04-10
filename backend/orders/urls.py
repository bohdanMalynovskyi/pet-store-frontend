from django.urls import path, include
from rest_framework import routers

from orders import views


router = routers.SimpleRouter()

router.register(r'orders', views.OrderViewSet, basename='orders')

urlpatterns = [
    path('warehouse/', views.get_warehouse, name='get-warehouse'),
    path('orders/create/', views.create_order, name='create_order'),
    path('', include(router.urls)),
               ]
