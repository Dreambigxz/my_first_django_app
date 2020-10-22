from django.shortcuts import (render, HttpResponse,
                              get_object_or_404, redirect, resolve_url,
                              reverse,)
from django.contrib.auth import authenticate, login, logout
from django.views.generic.edit import ProcessFormView
from django.views.generic.edit import FormView, View
from django.contrib.auth.tokens import default_token_generator
from django.urls import reverse_lazy
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView
from django_email_verification import sendConfirm
from django.core.mail import send_mail
from .models import MyUser
from django.contrib import messages
from .forms import UserCreationForm, UserLoginForm, UserResetPassword, PasswordResetForm
from .myfunc import timestamp_Otp_Verification
from myproject.decorators import redirect_auth_users
from django.http import JsonResponse
from userwallet.models import UserWallet
from django.contrib.auth import update_session_auth_hash

import datetime
# )

from django.core.exceptions import ValidationError

from django.conf import settings
from .models import MyUser, Testing


# Create your views here.


@redirect_auth_users
def reg(request):

    if request.method == 'GET' :
        print('yes')

    form= UserCreationForm

    if request.method == 'POST':

        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            user= form.save()

            userwallet=UserWallet.objects.get_or_create(user=user)

            token= (user.tokken)
            email= user.email

            print('yor emai address is ' + email + user.username)


            send_mail('Subject here',
                      'Please Verify your account with this One Time Pin {}'.format(token),
                      'from@example.com',
                      [email],
                      fail_silently=False)
            messages.info(request, 'Please check your email to use the OTP sent to you')
            return  redirect('account_verification')

        else:

            print('Form didnt save')


    else:

        form=UserCreationForm()


    return render(request, 'users/register.html', {'form': form})


@redirect_auth_users
def log_in(request):

    form=UserLoginForm()

    if request.method == 'POST':

        form= UserLoginForm(data=request.POST)

        email= request.POST.get('email')
        password= request.POST.get('password1')
        username= request.POST.get('username')

        user= authenticate(request, username=email, password=password )

        print(user)
        if user is not None:

            login(request, user)

            return redirect('product_store')


        check_if_user_acc_is_active= MyUser.objects.filter(email=email)
        for active in check_if_user_acc_is_active:
            if active.is_active== False:
                messages.info(request, 'Please verify your account to login')
                return redirect('account_verification')


    else:

        form= UserLoginForm()

    return render(request, 'users/login.html', {'form': form})


def log_out(request):

    logout(request)
    return redirect('product_store')

class VerifyAccount(View):


    def get(self, request):
        return render(request, 'users/verify_account.html')

    def post(self, request, *args, **kwargs):
        if request.method=='POST':
            user_token= request.POST.get('token')
            print(user_token)

            verify_user_token=MyUser.objects.filter(tokken=user_token)
            if verify_user_token.exists():
                for user in  verify_user_token:
                    if user.is_active== True:
                        messages.info(request, 'Your account has been verified please login')
                        return redirect('login')
                    else:
                        user.is_active=True
                        user.tokken= timestamp_Otp_Verification()
                        user.save()

                        if user.is_active== True:


                            print(user.email)
                            user_pass=(user.password)

                            check_pass= user.check_password('1111')
                            print(check_pass)
                            print(user_pass)
                            print("Our request type is " + request.method)



                            user_auth = authenticate(request, username=user.email, password='1111')

                            session=update_session_auth_hash(request, user)

                            print(session)


                            # if user_auth is not None:
                            #     login(request, user_auth)
                            #     return redirect('product_store')
                            # else:
                            #     print("There is no user ooo")

                            messages.info(request, 'Your account has been verified please login')
                            return redirect('login')


            else:
                messages.warning(request, 'Invalid Code Provided')

        return redirect('account_verification')



def validate_username(request):
    username= request.GET.get('username', None)

    print(username)
    data={'is_taken': MyUser.objects.filter(username__iexact=username).exists()}

    if data['is_taken']:
        data['error_message']= 'A user with this username already exist'
    return JsonResponse(data)