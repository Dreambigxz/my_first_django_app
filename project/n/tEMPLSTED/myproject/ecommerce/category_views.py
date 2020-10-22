from django.shortcuts import render, HttpResponse

from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import View

from .models import Products
# Create your views here.

class SportListView(ListView):

    context_object_name = 'sports'
    template_name = 'category/sport.html'

    def get_queryset(self):
        sports= Products.objects.filter(Cartegory='Sport')

        return sports


class FashionListView(ListView):

    context_object_name = 'fashions'
    template_name = 'category/fashion.html'

    def get_queryset(self):
        fashion= Products.objects.filter(Cartegory='Fashion')

        return fashion





class TrendingListView(ListView):

    context_object_name = 'trending'
    template_name = 'ecomm/home.html'

    def get_queryset(self):

        trending = {'women' : Products.objects.filter(Cartegory='Women'),

                     'men' : Products.objects.filter(Cartegory='Men'),

                    }

        return trending


class ProductDetailView(DetailView):
    model = Products
    template_name = 'ecomm/product_details.html'