from django.contrib import admin
from django.urls import path, include
from .views import show_cart
from cart import api


urlpatterns = [
    path('add_to_cart/', api.api_add_product_tocart, name='api_add_to_cart'),
    path('show_cart/',  show_cart, name='cart_detail'),
    path('remove_item/', api.api_remove_item, name='remove_from_cart'),
    path('incremente_quantity/', api.api_increment_quatity, name='api_incremente_quatity'),
    path('get_products/', api.api_get_products, name='api_get_products'),

    ## checkout 
    path('checkout)', api.checkout_cart, name='checkout'),
]