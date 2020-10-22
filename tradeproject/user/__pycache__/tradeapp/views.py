from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.views.generic import (View, TemplateView)
# Create your views here.

class HomeView(TemplateView):

    template_name = 'trade/home.html'

