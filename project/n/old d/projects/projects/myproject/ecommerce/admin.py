from django.contrib import admin
from .models import Products, Orderitem, Order, ShippingAddress, Rating, SubImages, ProductReviews


# Register your models here.


class ProductsAdmin(admin.ModelAdmin):

    fields = ('product_name', 'Cartegory', 'price', 'product_image','color')
    list_display = ('product_name', 'Cartegory', 'price', )

admin.site.register(Products, ProductsAdmin)
admin.site.register(Orderitem)
admin.site.register(Order)
admin.site.register(ShippingAddress)
admin.site.register(Rating)
admin.site.register(SubImages)
admin.site.register(ProductReviews)
