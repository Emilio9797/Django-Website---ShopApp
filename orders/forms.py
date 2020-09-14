from django.forms import ModelForm, TextInput
from .models import Order




class NewOrderForm(ModelForm):
    class Meta:
        model = Order
        fields = ['first_name', 'second_name', 'email', 'address', 'postal_code', 'city', 'delivery']

        widgets = {
                'first_name': TextInput(attrs={'class': "form-control"}),
                'second_name': TextInput(attrs={'class': "form-control"}),
                'email': TextInput(attrs={'class': "form-control"}),
                'address': TextInput(attrs={'class': "form-control"}),
                'postal_code': TextInput(attrs={'class': "form-control"}),
                'city': TextInput(attrs={'class': "form-control"}),

            }
