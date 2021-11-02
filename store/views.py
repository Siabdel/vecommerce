from django.shortcuts import render, get_object_or_404, get_list_or_404

from store import models
# Create your views here.

def product_detail(request, slug):
    product = get_object_or_404(models.Product, slug=slug)
    return render(request, "store/product_detail.html", locals())


def category_detail(request, category_slug):
    category = get_object_or_404(models.Category, slug=category_slug)
    products = category.products.filter(is_featured=True)
    return render(request, "store/category_detail.html", locals())

def product_list(request):
    products = models.Product.objects.filter(is_featured=True)
    return render(request, "store/product_list.html", locals())
