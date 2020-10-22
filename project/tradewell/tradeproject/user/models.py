from django.db import models
import random


from datetime import date, datetime
from django.utils import timezone
import datetime
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)
from django.conf import settings
from django.core.exceptions import ValidationError
from .token_generator import otp_Verification
# Create your models here.

current_date = date.today()
verification_pin = (random.randint(45995, 67995))
print('today is', current_date)


class MyUserManager(BaseUserManager):
    def create_user(self,  email, username, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError('Users must have an email address or User Name')

        if not username:

            raise  ValidationError('Username exist')

        user = self.model(
            email=self.normalize_email(email),
            username=  username,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password=None):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(

            username= username,
            email= email,
            password=password,
        )


        user.set_password(password)
        user.is_admin = True
        user.is_active = True
        user.save(using=self._db)
        return user

class MyUser(AbstractBaseUser):

    username= models.CharField(verbose_name='User Name',
                                unique=True,
                                max_length=100,)
    full_name= models.CharField(max_length=200, null=True)
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )

    otp= models.CharField(max_length=6, default=otp_Verification())
    phone_number= models.IntegerField(default=123,)
    is_active = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)


    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username' ]

    def __str__(self):
        return self.email


    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin


