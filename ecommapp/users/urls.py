from django.urls import path

from . import views, authviews, myviews, multyviews
from django.contrib.auth import views as auth_views
from .forms import  UserResetPassword, UserChangePasswordForm


users= 'users'


urlpatterns=[


    path('register/', views.reg, name='register'),
    path('login/', views.log_in, name='login'),
    path('verify/', views.VerifyAccount.as_view(), name='account_verification'),
    # path('login-register/', multyviews.MultipleFormsAuth.as_view(redirect_authenticated_userz), name='login-register'),

    ####test###



    path('testuser/', multyviews.MultipleFormsDemoView.as_view(), name='t'),
    path('logout/', views.log_out, name='logout'),
    path('test/', myviews.SendMail, name='test'),
    # path('test/', myviews.SendMailView.as_view(), name='logout'),




############ Django Auth urls #################


    path('password_reset/', auth_views.PasswordResetView.as_view(
        template_name='password/password_reset_form.html',
        email_template_name='password/password_reset_email.html',
        form_class=UserResetPassword,
        success_url='sent'
        ), name= 'resetpassword'),

    path('password_reset/sent/', auth_views.PasswordResetDoneView.as_view(
        template_name='password/password_reset_sent.html',
    ), name= 'sent'),
##########################################################################

    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name='password/set_password.html',
        form_class= UserChangePasswordForm,
        success_url= 'sent'


), name= 'setpassword'),

    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name='users/login.html'), name= 'resetform'),

#########################################JSON ROUTH################################################################################
    path('validate_username/', views.validate_username, name='validate_username')



]