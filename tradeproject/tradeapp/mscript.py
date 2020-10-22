from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.views.generic import (View, TemplateView)
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Capital, Unpaid_user, Paid_user


##my views


