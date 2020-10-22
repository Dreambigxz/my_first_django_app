from django.db import models
from django.urls import reverse
from django.utils import  timezone
from django.conf import settings

# Create your models here.

class Products(models.Model):

    All = 'Al'
    Sport = 'SP'
    Fashion = 'FS'
    Electronic = 'EL'
    Computer = 'CM'
    Beauty = 'BT'
    Baby = 'BY'

    Top_10 = 'T1'
    Women = 'WM'
    Men = 'MN'
    Kids = 'KD'
    Accessoriess = 'ACR'

    cartigories = [

            ('POPULAR CATEGORIES',(
              ('Fashion','Fashion'),
              ('Electronics','Electronics'),
              ('Computer','Computer'),
              ('Beauty','Beauty'),
              ('Sport','Sport'),

            )

         ),

        ('TRENDING PRODUCTS', (
            ('Top_10', 'Top_10'),
            ('Womens', 'Womens'),
            ('Mens', 'Mens'),
            ('Kids', 'Kids'),
            ('Accessories', 'Accessories'),

        )

         ),

        ('NEW ARRIVAL', (
            ('Televisons', 'Televisons'),
            ('Computer', 'Computer'),
            ('Jewelry', 'Jewelry'),
            ('Apparel', 'Apparel'),
            ('Apparel', 'Apparel'),



            )

         )

]


    product_name= models.CharField(max_length=200, null=True, blank=True)
    product_image= models.ImageField(null=True, blank=True)
    product_description= models.TextField(max_length=200, null=True, blank=True)
    rating = models.IntegerField(default=1, null=True, blank=True)
    price= models.FloatField(default=0, null=True)
    Cartegory = models.CharField(max_length=30, choices=cartigories, default='Top_10')
    slug= models.SlugField(null=True, blank=False, help_text='Please put a url name')



    def __str__(self):

        return self.product_name

    def get_absolute_url(self):
        return reverse('product', kwargs={
            'slug': self.slug})


class Orderitem(models.Model):

    item = models.ForeignKey(Products, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):

        return str(self.item.product_name)








class Order(models.Model):

    user= models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='user')
    ordered= models.BooleanField(default=False)
    orderitem = models.ManyToManyField(Orderitem, )
    start_date= models.DateTimeField(auto_now=True)
    ordered_date = models.DateTimeField(default=timezone.now)

    def __str__(self):

        return str(self.user.username)
