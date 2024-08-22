from django.urls import path, include
from rest_framework import routers

from orders import views

router = routers.SimpleRouter()

router.register(r'orders', views.OrderViewSet, basename='orders')

urlpatterns = [
    path('warehouse/', views.get_warehouses, name='get-warehouses'),
    path('warehouse-types/', views.get_warehouse_types, name='get-warehouse-types'),
    path('areas/', views.get_settlement_areas, name='get-settlement-areas'),
    path('settlements/', views.get_settlements, name='get-settlements'),
    path('orders/create/', views.create_order, name='create_order'),
    path('', include(router.urls)),
    path('approve_payment/', views.approve_payment, name='approve_payment')
]
