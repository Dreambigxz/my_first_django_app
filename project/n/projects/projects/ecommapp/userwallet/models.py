from django.db import models
from django.conf import settings
from users.myfunc import timestamp_Otp_Verification
from users.myfunc import account_number_generator


# Create your models here.


class UserWallet(models.Model):

    user= models.ForeignKey(settings.AUTH_USER_MODEL, related_name='userwallet', on_delete=models.CASCADE)
    account_number=models.IntegerField(default=account_number_generator())
    balance=models.FloatField(max_length=30, default=0)

    def __str__(self):
        return self.user.email



class WalletTransactions(models.Model):

    pass