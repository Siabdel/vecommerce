# -*- coding: utf-8 -*-
from django.shortcuts import render

# Create your views here.


def home(request):
    context = {}
    #
    return render(request, 'home/home.html', context)

def contact_form(request):
    return render(request, 'home/contact.html', locals())

def about(request):
    return render(request, 'home/about.html', locals())