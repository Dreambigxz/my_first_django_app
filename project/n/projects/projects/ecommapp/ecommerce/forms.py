from django.forms import forms
from django import forms
from django.forms import ModelForm
from .models import ShippingAddress


class ShippingAddressForm(ModelForm):

    class Meta():
        model= ShippingAddress
        fields= ('full_name', 'mobile_phone_number', 'address', 'state_of_origin')