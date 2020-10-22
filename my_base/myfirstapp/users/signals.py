from django.db.models.signals import (
    pre_save,  post_save)
from django.dispatch import receiver
from .models import MyUser


@receiver(post_save,  weak=False, sender=MyUser)
def my_handler(sender, **kwargs):
    print('pass')

