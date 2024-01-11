from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path('',views.foodlensFunction,name='FoodLens'),
    path('imageresult',views.foodlensresultFunction,name='foodLensResult')
    
]
