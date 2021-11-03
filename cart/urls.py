from django.contrib import admin
from django.urls import path, include
from .api import api_add_product_tocart
from .views import show_cart


urlpatterns = [
    path('add_to_cart/', api_add_product_tocart, name='api_add_to_cart'),
    path('show_cart/', show_cart, name='cart_detail'),
]