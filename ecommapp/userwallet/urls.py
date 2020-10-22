from django.urls import path
from . import views
from .views import UserWalletViews

app_label='userwallet'
urlpatterns=[

    path('my-wallet/', views.UserWalletViews.as_view(), name='my-wallet'),
    path('user_deposit/', views.Deposit.as_view(), name='user_deposit'),


]