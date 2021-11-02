

from django.conf import settings

session_di = settings['SESSION_COOKIES_AGE']

class cart(object):
    def __init__(self, request) -> None:
        cart  = request.session.get(settings.SESSION_COOKIES_AGE)
        self.session = request.session

        if not cart :
            cart = self.session[settings.CART_SESSION_ID] = {}
        
        self.cart = cart 
    
        

    def add(self, product, quantity=1, update_quantity=False ):
        product_id  = str(product.id)
        price = product.price 

        if product_id not in self.cart:
            self.cart[product_id] = {'id': product_id,  'price' : price, 'quantity' : 0 }

        if update_quantity :
            self.cart[product_id]['quantity'] = quantity
        else :
            self.cart[product_id]['quantity'] = quantityself.cart[product_id]['quantity'] + 1



    def save(self):
        self.session[session.CART_SESSION_ID] = self.cart
