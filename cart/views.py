from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.core import serializers
import json
from store import models
from .cart import Cart
from core.utils import JsonResponseMixin, django_query_serializable


def show_cart(request):
    """
    cart details
    """
    products = []

    cart_items = Cart(request)
     
    #products = cart_items.json_export(cart_items)
    #products = export_to_json(cart_items)
    """"
    for elem in cart_items :
        product = elem['product']
        #json_data = serializers.serialize('json', queryset)
        products.append(product)
    """
    #json_data = serializers.serialize('json', products)
    
    
    return render(request, 'cart/view_cart.html', locals())

 

def update_object(obj, **kwargs):
    # new_instance = new_class.__class__()
    for k, v in kwargs.items():
        setattr(obj, k, v)
##
##
def export_to_json(queryset):
    products = []

    for elem in queryset :
        product = elem['product']
        row = dict.fromkeys(product.__dict__, '')
        values = dict.values(product.__dict__)
        ligne  = dict(zip(row, values))
        ligne.__delitem__('_state')
        products.append(ligne)
        

    # dictOfWords = dict.fromkeys(listOfStr , 1)
    # new_p = dict(zip(row, values))
    return json.dumps(products)