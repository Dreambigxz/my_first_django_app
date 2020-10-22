from django.shortcuts import (render, HttpResponse,
                              get_object_or_404, redirect, resolve_url,
                              reverse,)
from django.contrib.auth import authenticate, login, logout
from django.views.generic.edit import ProcessFormView
from django.views.generic.edit import FormView
from django.contrib.auth.tokens import default_token_generator
from django.urls import reverse_lazy
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView
from django_email_verification import sendConfirm
from django.core.mail import send_mail
from .forms import UserCreationForm, UserLoginForm, UserResetPassword, PasswordResetForm


# )

from django.core.exceptions import ValidationError

from django.conf import settings
from .models import MyUser


# Create your views here.



def reg(request):

    if request.method == 'GET' :
        print('yes')

    form= UserCreationForm

    if request.method == 'POST':

        form = UserCreationForm(data=request.POST)
        email = request.POST.get('email')

        if form.is_valid():
            user= form.save()

            print('yor emai address is ' + email + user.username)


            send_mail('Subject here',
                      'Here is the message.',
                      'from@example.com', [email],
                      fail_silently=False)



            #send the mail now
            # sendConfirm(user)

            return  redirect('home')

        else:

            print('Form didnt save')


    else:

        form=UserCreationForm()


    return render(request, 'users/register.html', {'form': form})



def log_in(request):

    form=UserLoginForm()

    if request.method == 'POST':

        form= UserLoginForm(data=request.POST)

        email= request.POST.get('email')
        password= request.POST.get('password1')
        username= request.POST.get('username')

        user= authenticate(request, username=email or username, password=password )

        if user is not None:

            login(request, user,)

            return redirect('product_store')

    else:

        form= UserLoginForm()

    return render(request, 'users/login.html', {'form': form})


def log_out(request):

    logout(request)
    return render(request, 'rapp/index.html')


def reset_password(request):


    if request.method=='POST':
        form= PasswordResetForm(data=request.POST)

        if form.is_valid():
            email= form.cleaned_data.get('email')
            print(email)

    else:
        form= PasswordResetForm()
    return render(request, 'tpassword/password_reset_form.html', {'form', form})


