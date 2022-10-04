from django.urls import path, include
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('burgers/', cat_burger, name="burgers"),
    path('panini/', cat_panini, name="panini"),
    path('bageta/', cat_bageta, name="bageta"),
    path('salad/', cat_salad, name="salad")
]