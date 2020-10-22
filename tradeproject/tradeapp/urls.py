from . import views
from django.urls import path

app_name= 'trade'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('dashboard', views.UserDashboard.as_view(), name='dashboard'),
    path('accounts', views.UserAccount.as_view(), name='accounts'),
    path('settings', views.UserSettings.as_view(), name='settings'),
    path('transactions', views.UserTransactions.as_view(), name='transactions'),


]
