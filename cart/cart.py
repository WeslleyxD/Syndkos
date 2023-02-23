from decimal import Decimal
from django.conf import settings
from products.models import Product

class Cart(object):
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID, None)
        if not cart:
        # save an empty cart in the session
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart


    def add(self, product, quantity=1):
        product_id = str(product.id)
        if product_id not in self.cart:
            self.cart[product_id] = {'quantity': 0, 'value': str(product.value)}

        self.cart[product_id]['quantity'] += quantity

        self.save()


    def update(self, product, quantity):
        product_id = str(product.id)
        if product_id in self.cart:
            quantity_after = self.cart[product_id]['quantity'] + quantity
            if not quantity_after < 1:
                self.cart[product_id]['quantity'] += quantity
                self.save()
            else:
                self.remove(product)


    def save(self):
        self.session.modified = True


    def remove(self, product):
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()


    def __iter__(self):
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids)

        cart = self.cart.copy()
        for product in products:
            cart[str(product.id)]['product'] = product

        for item in cart.values():
            item['value'] = Decimal(item['value'])
            item['total_price'] = item['value'] * item['quantity']
            yield item


    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())


    def get_total_price(self):
        return sum((Decimal(item['value'])) * item['quantity'] for item in self.cart.values())
        

    def get_quantity_products(self):
        return len(self.cart)


    def clean(self):
        del self.session[settings.CART_SESSION_ID]
        self.save()



