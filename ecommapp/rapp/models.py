from django.db import models
from django.conf import settings
from django.utils import timezone
from django.urls import reverse

#from users.models import MyUser
# Create your models here.


class Restaurant(models.Model):
    food_name= models.CharField(max_length=100, null=True)
    food_image= models.ImageField(default=0)
    price= models.FloatField(default=0.0)
    description= models.CharField(max_length=200)


    def __str__(self):

        return self.food_name

    @property
    def imageURL(self):

        try:
            url= self.food_image.url
        except:
            url= ''

        return url

    def get_absolut_url(self):
        return reverse('home')




class Reservation(models.Model):
    user= models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,default=0)
    restaurant= models.OneToOneField(Restaurant, on_delete=models.CASCADE, default=0)
    expected_date= models.DateField(auto_now=False)
    expected_time= models.TimeField()
    total_person= models.IntegerField(default=0)
    message= models.TextField(max_length=200, null=True)
    date_created= models.DateField(default=timezone.now)
    completed= models.BooleanField(default=False)



    def __str__(self):

        return self.user.email


class Order(models.Model):
    user= models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    date_ordered= models.DateField(default=timezone.now)
    order_completed= models.BooleanField(default=False)
    transaction_id = models.CharField(max_length=200)

    def __str__(self):

        return str(self.user.email)

    def get_cart_total(self):

        orderitems= self.orderitem_set.all()
        total= sum([item.total() for  item in orderitems])

        return total

    def get_cart_items(self):

        orderitems= self.orderitem_set.all()
        total= sum([item.quantity for  item in orderitems])

        return total


class Orderitem(models.Model):
    food_name = models.ForeignKey(Restaurant, on_delete=models.CASCADE, blank=True, null=True)
    order= models.ForeignKey(Order, on_delete=models.CASCADE, blank=True, null=True)
    quantity= models.IntegerField(default=0, blank=True)
    date_added= models.DateField(auto_now=True)




    def __str__(self):

        return str(self.order)

    def total(self):

        totals= self.food_name.price * self.quantity
        print(totals)
        return totals

    # def sum_quantity(self):
    #
    #     sum_quantity= sum([items.quantity for items in Orderitem.objects.all()])
    #
    #     print(sum_quantity)
    #     return sum_quantity





class ShippingAddress(models.Model):
    Abia = 'FR'
    Delta = 'SO'
    Lagos = 'JR'
    Bauchi = 'SR'
    FCT = 'GR'
    Cities = [
        (Abia, 'Abia'),
        (Delta, 'Delta'),
        (Lagos, 'Lagos'),
        (Bauchi, 'Bauchi'),
        (FCT, 'FCT'),
    ]
    user= models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,default=0, blank=True)
    order= models.ForeignKey(Order, on_delete=models.CASCADE, blank=True, null=True)
    address= models.CharField(max_length=200, blank=True)
    city= models.CharField(max_length=5, choices=Cities, default=Abia, blank=True)

    def __str__(self):
        return self.address


