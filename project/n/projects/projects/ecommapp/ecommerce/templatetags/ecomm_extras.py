from django import template
from ecommerce.models import ShippingAddress
from  ecommerce.forms import ShippingAddressForm
register = template.Library()

def upper(value): # Only one argument.
    """Converts a string into all lowercase"""
    return value.upper()

# @register.filter
# def upper(value):
#     return value.upper()

# def cut(value, arg):
#     """Removes all values of arg from the given string"""
#     return value.replace(arg, '')
#
register.filter('uper', upper)


# def addexist(request,):
#
#
#
#
# register.filter('addexist', addexist)