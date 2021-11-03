
import json
from django.http.response import JsonResponse
from django.shortcuts import render, get_object_or_404
from .cart import Cart
from store.models import Product

# Create your views here.


def cart_home(request):
    return render(request, 'cart/cart.html')

def api_add_product_tocart(request):
    """
    add a article to cart with session cookies
    vuejs POST {'product_id': id, 'quantity':1} to cart_add
    """
    json_reponse = { 'success': False}
    data = json.loads(request.body)
    
    product_id  = data.get('product_id')
    if not product_id :
        return JsonResponse(json_reponse)

    update = request.POST.get('update')
    quantity = request.POST.get('quantity', 1)
   
   ## print 
    print("#### debug ####")
    print(data)
    print( product_id )


    ## cart cookies
    cart = Cart(request)
    product = get_object_or_404(Product, pk=product_id)

    if not update :
        cart.add(product, quantity=1, update_quantity=False)
    else :
        cart.add(product, quantity=quantity, update_quantity=True)

    json_reponse = { 'success': True}
    
    return JsonResponse(json_reponse)

def remove_product(request):
    """
    """
    pass