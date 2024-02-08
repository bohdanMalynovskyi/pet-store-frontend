from django.urls import path, include
from rest_framework import routers

from categories import views

router = routers.SimpleRouter()
router.register(r'animalcategories', views.AnimalCategoryViewSet, basename='animalcategory')
router.register(r'productcategories', views.ProductCategoryViewSet, basename="productcategory")
router.register(r'subcategories', views.SubCategoryViewSet, basename='subcategory')

urlpatterns = [
    path('', include(router.urls))
]
