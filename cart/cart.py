from decimal import Decimal
from django.conf import settings
from store.models import ShopItem
from django.db import models
from store.models import ShopItem, DeliveryOption

class Cart(object):

    def __init__(self, request):
        self.session = request.session

        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}

        self.cart = cart

    def __iter__(self):
        item_ids = self.cart.keys()
        items = ShopItem.active_items.filter(id__in=item_ids)
        cart = self.cart.copy()

        for item in items:
            self.cart[str(item.id)]['item'] = item

        for cart_item in cart.values():
            cart_item['price'] = Decimal(cart_item['price'])
            cart_item['total_cost'] = cart_item['price'] * cart_item['quantity']
            yield cart_item

    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())

    def get_total_price(self):
        return sum(item['total_cost'] for item in self.cart.values())


    def add(self, item, quantity=1, update_quantity=False):
        item_id = str(item.id)

        if item_id not in self.cart:
            self.cart[item_id] = {'quantity': 0, 'price': str(item.price)}

        if update_quantity:
            self.cart[item_id]['quantity'] = quantity
        else:
            self.cart[item_id]['quantity'] += quantity
        self.save()

    def remove(self, item):
        item_id = str(item.id)

        if item_id in self.cart:
            del self.cart[item_id]
            self.save()

    def save(self):
        self.session.modified = True

    def clear_cart(self):
        del self.session[settings.CART_SESSION_ID]
        self.save()

