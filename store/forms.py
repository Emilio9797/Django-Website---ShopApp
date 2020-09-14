from django import forms

class SendEmailForm (forms.Form):
    name = forms.CharField(max_length=50, min_length=4,
                           widget=forms.TextInput(attrs={'placeholder': "Your Name", 'class': "form-control"}))
    email = forms.EmailField(widget=forms.TextInput(
        attrs={'class': "form-control", 'name': "email", 'placeholder': "Your Email", 'data-error': "Please enter Your Email"}))
    subject = forms.CharField(max_length=50, min_length=3, widget=forms.TextInput
        (attrs={'class': "form-control", 'name': "subject", 'placeholder': "Subject of the message", 'data-error': "Please enter Your name"}))
    message = forms.CharField(max_length=2000, widget=forms.TextInput
        (attrs={'class': "form-control", 'id': "message", 'placeholder': "Your message:", 'data-error': "Write Your message", 'rows': "4"}))

    send_copy = forms.BooleanField(label="Would You like a copy of a message?   ", initial=False, required=False)


class SearchForm(forms.Form):
    slug = forms.CharField(max_length=20, min_length=2, label=False, initial='Search here...')
