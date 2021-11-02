
from django.contrib import admin
from django.urls import path, include
from core.views import about, home, contact_form
from store import views


urlpatterns = [
    path('', home, name='homepage'),
    path('contact/', contact_form, name='contact'),
    path('about/', about, name='about'),
]
