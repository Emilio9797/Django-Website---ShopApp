from django.db import models
from store.models import ShopItem, DeliveryOption
from cart.cart import Cart
from decimal import Decimal


class Order(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    paid = models.BooleanField(default=False)

    first_name = models.CharField(max_length=40 )
    second_name = models.CharField(max_length=40)
    email = models.EmailField()
    address = models.CharField(max_length=250)
    postal_code = models.CharField(max_length=15)
    city = models.CharField(max_length=50)
    delivery = models.ForeignKey(DeliveryOption, on_delete=models.CASCADE, default=DeliveryOption.objects.first().pk)
    class Meta:
        ordering = ('-date_created',)

    def __str__(self):
        return 'Order {}'.format(self.id)

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.ordered_items.all())

    def get_total_cost_with_delivery(self):
        return self.get_total_cost() + self.delivery.price

    def create_order(self, request):
        for item in Cart(request):
            self.ordered_items += item


class OrderedItem (models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='ordered_items')
    item = models.ForeignKey(ShopItem, on_delete=models.CASCADE, related_name='item')
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return str(self.item.id)

    def get_cost(self):
        return self.price * self.quantity

