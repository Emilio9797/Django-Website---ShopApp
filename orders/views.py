from django.shortcuts import render
from .forms import NewOrderForm
from .models import OrderedItem
from cart.cart import Cart
from .tasks import order_created
from django.core.mail import send_mail

def create_order_view(request):
    cart = Cart(request)

    if request.method == 'POST':
        form = NewOrderForm(request.POST)
        if form.is_valid():
            order = form.save()
            cart = Cart(request)

            #order.delivery = cart.delivery

            for item in cart:
                OrderedItem.objects.create(order=order,
                                           item=item['item'],
                                           quantity=item['quantity'],
                                           price=item['price'])
            cart.clear_cart()
            order_created.delay(order.id)

            #mail to customer:
            send_mail('Order number {} has been completed!'. format(str(order.id)),
                      'Thank you for placing order at HappySkullPainting! \n \n Another email will follow soon, containg all the details. \n \n Cheers,\n Emil',
                      'happyskullpainting@gmail.com', [order.email], fail_silently=True)
            #mail for shop
            send_mail('You have an order {}, do smth about it!'.format(str(order.id)), 'You have an order {}, do smth about it!'.format(str(order.id)),'happyskullpainting@gmail.com', ['eemil.kklonowski@gmail.com', 'happyskullpainting@gmail.com'], fail_silently=True)
            return render(request, 'store/checkout-completed.html', {'order': order})
    else:
        form = NewOrderForm()
        #delivery_form = UpdateOnChangeDelivery()
        return render(request, 'store/checkout.html', {'cart': cart, 'form': form})






