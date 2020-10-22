from django.shortcuts import render, HttpResponse

from django.views.generic import TemplateView, ListView, DetailView

from .models import Products

# Create your views here.






class HomeListView(ListView):

    context_object_name = 'products'
    template_name = 'ecomm/home.html'


    def get_queryset(self):

        AllHomeCartegoriesKwargs = {'women' : Products.objects.filter(Cartegory='Womens'),
                    'top_10': Products.objects.filter(Cartegory='Top_10'),
                    'tele': Products.objects.filter(Cartegory='Televisons')

                    }

        return AllHomeCartegoriesKwargs



class ProductDetailView(DetailView):

    template_name = 'ecomm/product-details.html'
    model = Products
