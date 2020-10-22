from . import views
from django.urls import path

urlpatterns=[

    path('signin/', views.Signin.as_view(), name='sign_in'),
    path('signup/', views.Signup.as_view(), name='sign_up'),
    path('lost_session', views.Logout.as_view(), name='logout'),
    path('account_verification/', views.Account_verification.as_view(), name='account_verification'),
    path('forgot_password/', views.LostPassword.as_view(), name='forgot_password'),

]