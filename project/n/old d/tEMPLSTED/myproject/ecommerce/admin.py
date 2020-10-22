from django.contrib import admin
from .models import Products, Orderitem, Order


# Register your models here.


admin.site.register(Products)
admin.site.register(Orderitem)
admin.site.register(Order)
