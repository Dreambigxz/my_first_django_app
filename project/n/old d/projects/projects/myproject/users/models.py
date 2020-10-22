from django.db import models
import random
# import sys
# sys.setrecursionlimit(10**6)


from datetime import date, datetime
from django.utils import timezone
import datetime
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)
from django.conf import settings
from django.core.exceptions import ValidationError
from .myfunc import timestamp_Otp_Verification
# Create your models here.

current_date = date.today()
verification_pin = (random.randint(45995, 67995))
print('today is', current_date)


class MyUserManager(BaseUserManager):
    def create_user(self,  email,  date_of_birth, username, password=None):
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
            date_of_birth=date_of_birth,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, date_of_birth, username, password=None):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(

            username= username,
            email= email,
            password=password,
            date_of_birth=date_of_birth,
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

    # date_join= models.DateField(auto_now=False)
    has_got_mail= models.BooleanField(default=False)
    expired= models.BooleanField(default=False)
    date_of_birth = models.DateField(null=True, )
    tokken= models.CharField(max_length=20, default=timestamp_Otp_Verification,)
    phone_number= models.IntegerField(default=123)
    is_active = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)


    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['date_of_birth',
                       'username' ]

    def __str__(self):
        return self.email

    def expire(self):
        if self.date_join < datetime.date(year=current_date.year, month=current_date.month, day=current_date.day):

            self.expired= True
            self.save()
        else:
            self.expired= False
            self.save()

    # def mail_received(self):
    #
    #     if self.expired == False:
    #         self.has_got_mail = False
    #
    #         self.save()
    #
    #     else:
    #         self.has_got_mail= True
    #         self.save()

    # def save(self, *args, **kwargs):
    #
    #     if self.date_join < datetime.date(year=current_date.year, month=current_date.month, day=current_date.day):
    #         self.expired = True
    #         y = super(MyUser, self).save(args, kwargs)
    #         return y
    #     else:
    #         self.expired= False
    #         super(MyUser, self).save(args, kwargs)

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


class Testing(models.Model):

    name=models.CharField(max_length=200)
    age= models.IntegerField(default=0)

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None, *args, **kwargs):

        if self.age==0:
            self.age += 55
            super(Testing, self).save(args, kwargs)

        else:
            self.age=self.age
            super(Testing, self).save(args, kwargs)
