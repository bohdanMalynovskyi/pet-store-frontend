from django.urls import path, include
from rest_framework import routers

from products import views

router = routers.SimpleRouter()
router.register(r'changeableprices', views.ChangeablePriceViewSet, basename='changeableprices')
router.register(r'tags', views.TagsViewSet, basename='tags')
router.register(r'', views.ProductViewSet, basename='products')


urlpatterns = [path('', include(router.urls))]
