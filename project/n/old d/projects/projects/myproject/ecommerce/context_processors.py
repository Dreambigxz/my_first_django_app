from .models import Orderitem
from .models import Products
import json

def base(request):
    try:
        device = request.COOKIES['device']

    except:
        device = {}


    cart_total = ([i.quantity for i in Orderitem.objects.filter(device_name=device)])


    return {
        'cart_total': sum(cart_total),
    }


