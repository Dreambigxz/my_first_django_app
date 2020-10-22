from django.contrib import admin
from .models import Restaurant, Reservation, Order, Orderitem, ShippingAddress

# Register your models here.

admin.site.register(Restaurant)
admin.site.register(Reservation)
admin.site.register(Order)
admin.site.register(Orderitem)
admin.site.register(ShippingAddress)
