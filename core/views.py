from django.shortcuts import render

# Create your views here.


def home(request):
    context = {}
    #
    return render(request, 'home.html', context)

def contact_form(request):
    return render(request, 'contact.html', locals())