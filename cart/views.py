from django.shortcuts import render, get_object_or_404, redirect
from .forms import AddCartForm, UpdateOnChangeForm
from store.models import ShopItem
from .cart import Cart
from django.views.decorators.http import require_POST

@require_POST
def generic_add_view(request, item_id, form):
    item = get_object_or_404(ShopItem.active_items.filter(id=item_id))
    cart = Cart(request)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(item, quantity=cd['quantity'], update_quantity=cd['update_quantity'])

    return redirect('cart:cart_detail')


def add_view(request, item_id):
    form = AddCartForm(request.POST)
    return generic_add_view(request, item_id, form)


def add_onchange_view(request, item_id):
    form = UpdateOnChangeForm(request.POST)
    return generic_add_view(request, item_id, form)


def cart_remove(request, item_id):
    item = get_object_or_404(ShopItem.objects.filter(id=item_id))
    cart = Cart(request)
    cart.remove(item)
    return redirect('cart:cart_detail')


def cart_detail(request):
    cart = Cart(request)

    for item in cart:
        item['update_quantity_form'] = UpdateOnChangeForm(initial={'quantity': item['quantity'],
                                                    'update_quantity': True})
    return render(request, 'store/cart.html', {'cart': cart})