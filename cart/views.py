from django.shortcuts import render, get_object_or_404, get_list_or_404

from store import models
from .cart import Cart

def show_cart(request):
    """
    cart details
    """
    cart_items = Cart(request)

    ## return render(request, 'cart/cart_detail.html', locals())
    return render(request, 'cart/view_cart.html', locals())
