from django.db import models
from django.conf import settings
from django.utils import timezone
from userwallet.models import Userwallet
# Create your models here.

class Capital(models.Model):

    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True,blank=True)
    user_capital = models.DecimalField(decimal_places=1, default=0, max_digits=500000)

    def __str__(self):
        return self.user.username

class AccountNumber(models.Model):
    pass


class Unpaid_user(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True,blank=True)
    date_join= models.DateTimeField(default=timezone.now)

    capital = models.ForeignKey(Capital, on_delete=models.CASCADE, null=True,blank=True)

    amount_to_pay= models.DecimalField(decimal_places=1, default=0, max_digits=500000)
    amount_merged= models.DecimalField(decimal_places=1, default=0, max_digits=500000)

    merged_to_pay= models.BooleanField(default=False)

    amount_payed= models.DecimalField(decimal_places=1, default=0, max_digits=500000)
    payment_completed= models.BooleanField(default=False)


    def __str__(self):
        return self.user.username


    class Meta:
        ordering=['date_join']


class Paid_user(models.Model):

    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='user',null=True, blank=True)
    user_account_number= models.ForeignKey(Userwallet, on_delete=models.CASCADE,null=True, blank=True)
    date_paid= models.DateTimeField(default=timezone.now)

    interest= models.DecimalField(decimal_places=1, default=0, max_digits=500000)

    amount_to_merge = models.DecimalField(decimal_places=1, default=0, max_digits=500000, blank=True, null=True)
    amount_merged= models.DecimalField(decimal_places=1, default=0, max_digits=500000)
    merged_to_receive = models.BooleanField(default=False)

    amount_received = models.DecimalField(decimal_places=1, default=0, max_digits=500000)
    received_completed = models.BooleanField(default=False)


    def __str__(self):
        return self.user.username


class Payer_transaction_table(models.Model):

    payer_details = models.ForeignKey(Unpaid_user, on_delete=models.CASCADE, null=True,blank=True)
    receiver_details = models.ForeignKey(Paid_user, on_delete=models.CASCADE ,null=True, blank=True)
    amount_to_pay= models.DecimalField(decimal_places=1, default=0, max_digits=500000)
    date= models.DateTimeField(default=timezone.now)
    completed= models.BooleanField(default=False)

    def __str__(self):
        return self.payer_details.capital.user.username


class Receivers_transaction_table(models.Model):

    receiver_details = models.ForeignKey(Paid_user, on_delete=models.CASCADE, null=True,blank=True)
    payer_details= models.ForeignKey(Unpaid_user, on_delete=models.CASCADE, null=True, blank=True)
    amount_to_receive= models.DecimalField(decimal_places=1, default=0, max_digits=500000)
    date = models.DateTimeField(default=timezone.now)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.receiver_details.user.username


