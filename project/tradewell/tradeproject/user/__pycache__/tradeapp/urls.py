from . import views
from django.urls import path

app_name= 'trade'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home')

]
