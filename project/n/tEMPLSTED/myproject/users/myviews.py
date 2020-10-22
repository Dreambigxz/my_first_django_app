from django.shortcuts import render, HttpResponseRedirect, HttpResponse, redirect
from django.db.models import Q

from django.views.generic.edit import FormView
from django.views.generic import  TemplateView, ListView, CreateView

from .myform import SendMailForm

from datetime import *
import datetime
from .models import MyUser
from django.contrib import messages
from django.core.mail import send_mail

# class SendMailView(CreateView):
#
#     template_name = 'users/test.html'
#     form_class = SendMailForm

def SendMail(request):

    email = MyUser.objects.values_list('email', flat=True)

    form= SendMailForm

    if request.method == 'POST':

        #get user and mesage data
        email=request.POST.get('email')
        admin_message=request.POST.get('message')


        send_mail(
            'Calling tasks is described in detail in the Calling Guide.subject',
            admin_message,
            'fromadmin@site.com',
            [email]

        )

        messages.success(request, 'message sent successfully')
        return redirect('test')




    return render(request, 'users/test.html', {'form': form, 'email':email}, )




# def checking_for_expired_users():
#     if True:
#
#         obj= MyUser.objects.all()
#
#         for i in obj:
#
#             print(i)
#
#             i.expire()
#
#
# def get_expired_users_and_send_mail():

# get_expired_users=MyUser.objects.filter(Q(expired=True) & Q(has_got_mail=False))
# for email in get_expired_users:
#
#
#     email.has_got_mail=True
#
#     email.save()
#
#     print(email.has_got_mail)

