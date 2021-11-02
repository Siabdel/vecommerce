
from django.contrib import admin
from django.urls import path, include
from core.views import home, contact_form
from store import views


urlpatterns = [
    
    ## STORE
    path('list/', views.product_list,  name='product_list'),
    path('<slug:slug>/', views.product_detail,  name='product_detail'),
    path('<slug:category_slug>/', views.category_detail, name='category_detail'),
]
