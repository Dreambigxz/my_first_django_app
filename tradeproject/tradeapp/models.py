from django.db import models
from django.conf import settings
from django.utils import timezone



# Create your models here.

class Capital(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True,blank=True)
    user_capital = models.DecimalField(decimal_places=1, default=0, max_digits=500000)

    def __str__(self):
        return self.user.username


class Unpaid_user(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True,blank=True)
    capital = models.DecimalField(decimal_places=1, default=0, max_digits=500000)
    amount_to_pay= models.DecimalField(decimal_places=1, default=0, max_digits=500000)
    amount_merged= models.DecimalField(decimal_places=1, default=0, max_digits=500000)
    merged_to_pay= models.BooleanField(default=False)
    merged_completed= models.BooleanField(default=False)
    account_paying_to= models.CharField(max_length=200, blank=True, null=True)
    payment_completed= models.BooleanField(default=False)

    def __str__(self):
        return self.user.username


class Paid_user(models.Model):

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='user',null=True, blank=True)
    user_account_number= models.CharField(max_length=30, blank=True, null=True)
    date_paid= models.DateTimeField(default=timezone.now)

    interest= models.DecimalField(decimal_places=1, default=0, max_digits=500000)
    amount_to_receive= models.DecimalField(decimal_places=1, default=0, max_digits=500000, blank=True, null=True)
    amount_merged= models.DecimalField(decimal_places=1, default=0, max_digits=500000)
    merged_to_receive = models.BooleanField(default=False)
    merged_completed = models.BooleanField(default=False)


    receiving_from= models.CharField(max_length=200, blank=True, null=True)
    payment_completed= models.BooleanField(default=False)

    def __str__(self):
        return self.user.username
