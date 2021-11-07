
import json
from django.http.response import JsonResponse
from django.shortcuts import render, get_object_or_404
from .cart import Cart
from store.models import Product
from django.conf import settings


# Create your views here.


def cart_home(request):
    return render(request, 'cart/cart.html')

def api_get_products(request):
    #
    data = []
    ## products = request.session[settings.CART_SESSION_ID] 
    products =  Cart(request)

    for elem in products :
        product = elem['product']
        row = dict.fromkeys(product.__dict__, '')
        values = dict.values(product.__dict__)
        ligne  = dict(zip(row, values))
        ligne.__delitem__('_state')
        ligne.__delitem__('created')
        # ajout quantite 
        ligne['quantity'] = elem['quantity']
        data.append(ligne)
    # dictOfWords = dict.fromkeys(listOfStr , 1)
    # new_p = dict(zip(row, values))
    #json_reponse = { 'success': False }

    return JsonResponse(data, safe=False)

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

def api_remove_item(request):
    """
    """
    json_reponse = { 'success': False}
    data = json.loads(request.body)
    product_id  = data.get('product_id')
    #print(product_id)
    #print(data)
    ## cart cookies
    cart = Cart(request)
    cart.remove(product_id)

    json_reponse = { 'success': True}
        
    return JsonResponse(json_reponse)

def checkout_cart(request):
    json_reponse = { 'success': True}
    return JsonResponse(json_reponse)

def  api_increment_quatity(request):
    cart = Cart(request)
    data = json.loads(request.body)
    #
    product_id  = data.get('product_id')
    quantity = data.get('quantity') 
    # qte ++
    print("avant" , quantity)
    if quantity :
        cart.update_qte(product_id, quantity)
    
    json_reponse = { 'success': True}
        
    return JsonResponse(json_reponse)


def api_get_items_count(request):
    products =  Cart(request)
    nbItems = sum(int(elem['quantity'])  for elem in products )
    json_reponse = { 
        'success': True,
        'cartShoppingCount' : nbItems,
    }
    return JsonResponse(json_reponse)