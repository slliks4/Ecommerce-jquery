from django import forms
from .models import *

class Add_shipping_address(forms.ModelForm):
    class Meta:
        model = Shipping_address
        fields = ['email','email_news','delivery_option','country','first_name','last_name','address','appartment','city']
        widgets = {
            'email': forms.EmailInput(attrs={'placeholder': 'Enter your email'}),
            'first_name': forms.TextInput(attrs={'placeholder': 'Enter your first name'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Enter your last name'}),
            'address': forms.TextInput(attrs={'placeholder': 'Enter your address'}),
            'appartment': forms.TextInput(attrs={'placeholder': 'Enter your apartment number'}),
            'city': forms.TextInput(attrs={'placeholder': 'Enter your city'}),
        }

class Complete_payment(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ['billing_address','remember_me']

class add_quantity(forms.ModelForm):
    class Meta:
        model = Order_items
        fields = ['quantity','selected']
        widgets = {
            'quantity' : forms.NumberInput(attrs={'class':'form_quantity'})
        }

class select(forms.ModelForm):
    class Meta:
        model = Order_items
        fields = ['selected',]