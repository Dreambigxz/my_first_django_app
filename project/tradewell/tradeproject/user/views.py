from django.shortcuts import render, redirect, HttpResponse
from django.urls import reverse
from django.views.generic import View,TemplateView
from .forms import UserCreationForm, UserLoginForm
from .models import MyUser
from .token_generator import otp_Verification
from  django.core.mail import send_mail
from django.db.models import Q
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .password_generator import forgot_password_generator
# Create your views here.

class Signin(View):

    def get(self, request):

        if self.request.user.is_authenticated:

            return redirect('trade:dashboard')

        else:
            return render(request, 'authentication/signin.html')

    def post(self, request):
        if request.method == 'POST':

            email= request.POST['email']
            password= request.POST['password']

            user = authenticate(request, username=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('trade:dashboard')

            else:

                messages.error(request, 'No user with the given credentials')
                return redirect('sign_in')

class Signup(View):

    def get(self, request):

        if self.request.user.is_authenticated:

            return redirect('trade:dashboard')

        else:
            forms= UserCreationForm

            return render(request, 'authentication/signup.html', {'forms': forms})


    def post(self, request):

        if request.method == 'POST':

            fullname= request.POST.get('fullname')

            username= request.POST.get('username')
            email= request.POST.get('email')
            number= request.POST.get('number')
            password= request.POST.get('password')


            if MyUser.objects.filter(Q(email=email) | Q(username=username)).exists():

                messages.info(request, 'User with this credentials alreasdy exist')
                return redirect('sign_up')
            else:
                user= MyUser.objects.create_user(username=username, email=email, password=password)

                user.full_name= fullname
                user.phone_number= number
                user.otp= otp_Verification()
                user.set_password(password)
                user.save()


            send_mail('Verify Account',
                      'Please Verify your account with this One Time Pin {}'.format(user.otp),
                      'info@tradewell.com',
                      [email],
                      fail_silently=False
                      )

            messages.info(request, 'Please check your provided email address to use the code sent to you from trade4')
            return redirect('account_verification')

class Account_verification(View):

    def get(self, request):

        if self.request.user.is_authenticated:

            return redirect('trade:dashboard')

        else:

            return render(request, 'authentication/account_verification.html')

    def post(self, request):

        if request.method=='POST':

            verification_pin= request.POST['verify_account']
            print(verification_pin)

            if MyUser.objects.filter(otp=verification_pin).exists():

                MyUser.objects.filter(otp=verification_pin).update(is_active=True)
                MyUser.objects.filter(otp=verification_pin).update(otp='v'+str(verification_pin))

                messages.success(request, 'Account Sucessfully veryfied')
                return redirect('sign_in')

            else:

                messages.error(request, 'Invalid code provided')
                return HttpResponse('invalid code provided')


class Logout(View):

    def get(self, request):

        logout(request)
        return redirect('trade:home')


class LostPassword(View):

    def get(self, request):

        if self.request.user.is_authenticated:

            return redirect('trade:dashboard')

        else:

            return render(request, 'password/forgot_password.html')

    def post(self, request):

        if request.method == 'POST':

            user_email= request.POST['email']

            print(user_email)

            #check if the given email exist update the password and send it to the user mail

            user= MyUser.objects.filter(email=user_email)

            if user.exists():

                for password in user:

                    reset_password= forgot_password_generator()
                    password.set_password(reset_password)

                    password.save()
                    send_mail('Reset Password',
                              'Please login with the password to reset your account {}'.format(reset_password),
                              'info@tradewell.com',
                              [user_email],
                              fail_silently=False
                              )
                    messages.success(request, 'Code Sent')
                    return redirect('forgot_password')

            else:
                return HttpResponse('no user exist')