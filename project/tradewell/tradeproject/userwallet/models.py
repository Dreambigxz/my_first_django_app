from django.db import models
from django.conf import settings
from user.token_generator import account_number_generator
# Create your models here.


class Userwallet(models.Model):

    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True,blank=True)
    user_balance= models.DecimalField(decimal_places=1, default=0, max_digits=500000)
    user_account_number = models.IntegerField(default=account_number_generator())


    def __str__(self):
        return self.user.username