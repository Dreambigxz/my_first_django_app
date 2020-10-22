# Create your tasks here

from __future__ import absolute_import, unicode_literals
from celery import shared_task
from celery.utils.log import get_task_logger
from users.models import MyUser
from django.core.mail import send_mail
from django.db.models import Q


from .models import current_date
logger = get_task_logger(__name__)

# from users.myviews import checking_for_expired_users, get_expired_users_and_send_mail

@shared_task
def check_if_user_has_expired():
    obj = MyUser.objects.all()

    for i in obj:
        i.expire()

@shared_task
def get_expired_users_and_send_mail():

    get_expired_users = MyUser.objects.filter(Q(expired=True) & Q(has_got_mail=False))

    for email in get_expired_users:

       user_email=email
       admin_message='Your due has expired today please renew it'


       if user_email.has_got_mail == False:

           send_mail(
               'Expired Due',
                admin_message,
               'fromadmin@site.com',
               [user_email],
           )

           user_email.has_got_mail = True

           user_email.save()


@shared_task
def get_paid_users_and_send_mail():

    get_paid_users= MyUser.objects.filter(Q(expired=False) & Q(has_got_mail=True))

    for user in get_paid_users:

        myuser= user
        admin_message = 'SUCCESSFULLY RENEW'

        if user.has_got_mail == True:

            send_mail(
                'RENEWD RENT',
                admin_message,
                'fromadmin@site.com',
                [myuser.email],
            )

            myuser.has_got_mail = False
            myuser.save()

        else:
            pass









