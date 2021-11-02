from .models import Category
from django.shortcuts import render



def menu_categories(request):
    categories = Category.objects.all()
    return { 'menu_categories' : categories}
