

from django.conf import settings
from store.models import Product
 
class Cart(object):

    def __init__(self, request) -> None:
        cart  = request.session.get(settings.CART_SESSION_ID)
        self.session = request.session

        if not cart :
            cart = self.session[settings.CART_SESSION_ID] = {}
        
        self.cart = cart 
    
    def __iter__(self):
        product_ids =  self.cart.keys()
        product_clean_ids = []

        for elem in product_ids :
            product_clean_ids.append(elem)
            self.cart[str(elem)]['product'] =  Product.objects.get(pk=elem)

        for item in self.cart.values() :
            item['total'] = int(item['price']) * int(item['quantity'])
            yield item



    def __len__(self):
        # la somme des quanitity integreé dans le panier
        return sum( item['quantity'] for item in self.cart.values())
        

    def add(self, product, quantity=1, update_quantity=False ):
        product_id  = str(product.id)
        price = product.price 

        if product_id not in self.cart:
            self.cart[product_id] = {'id': product_id,  'price' : price, 'quantity' : 0 }

        if update_quantity :
            self.cart[product_id]['quantity'] = quantity
        else :
            self.cart[product_id]['quantity'] = self.cart[product_id]['quantity'] + 1
        ## save 
        self.save()



    def save(self):
        self.session[settings.CART_SESSION_ID] = self.cart
