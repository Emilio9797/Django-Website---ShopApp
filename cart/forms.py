from django import forms
from store.models import DeliveryOption
from cart.cart import Cart

PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1,5)]

class AddCartForm(forms.Form):
    quantity = forms.TypedChoiceField(choices=PRODUCT_QUANTITY_CHOICES, coerce=int)
    update_quantity = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)


class UpdateOnChangeForm(forms.Form):
    quantity = forms.TypedChoiceField(choices=PRODUCT_QUANTITY_CHOICES, coerce=int, widget=forms.Select(attrs={'onchange': 'this.form.submit();'}))
    update_quantity = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)


class UpdateOnChangeDelivery(forms.Form):
    class Meta:
        model = Cart
        fields = ['delivery']