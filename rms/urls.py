from django.contrib import admin
from django.urls import path
from . import views
from rest_framework import routers

router=routers.SimpleRouter()
router.register('categories',views.CategoryViewSet)
router.register('foods',views.FoodViewset)

urlpatterns = [
 
]+router.urls