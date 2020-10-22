from django.test import TestCase

# Create your tests here.
from django.conf import settings
from django.core.mail import EmailMessage, send_mail
settings.configure()
from django.core.mail import send_mail

if True:
    send_mail(
        'Subject here',
        'Here is the message.',
        'from@example.com',
        ['to@example.com'],
        fail_silently=False,
    )