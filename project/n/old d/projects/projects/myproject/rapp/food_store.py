from django.shortcuts import render
from django.http import JsonResponse
import json
from django.views.generic import (TemplateView, CreateView,
                                  DeleteView, DetailView,
                                  ListView)
from .models import *

class basehtml(ListView):

    template_name = 'rapp/base.html'
    context_object_name = 'cart_item'

    def get_queryset(self):

        if self.request.user.is_authenticated:
            # print(self.request.user)

            try:
                order, created = Order.objects.get_or_create(user=self.request.user)

                items = {'items': order.orderitem_set.all(),
                         'order': order}
                return items

            except:
                []

class RestaurantFoodView(ListView):

    template_name = 'rapp/index.html'
    model =  Restaurant


class CartListView(ListView):

    template_name = 'rapp/store/cart.html'
    context_object_name = 'cart'

    def get_queryset(self):

        if self.request.user.is_authenticated:
            #print(self.request.user)

            try:
                order, created= Order.objects.get_or_create(user=self.request.user)


                items= {'items': order.orderitem_set.all(),
                        'order': order}

                return items
            except:

                []

        else:
            []

class CheckoutListView(ListView):

    template_name = 'rapp/store/checkout.html'

    context_object_name = 'checkout'

    def get_queryset(self):

        if self.request.user.is_authenticated:
            # print(self.request.user)

            try:
                order, created = Order.objects.get_or_create(user=self.request.user)

                items = {'items': order.orderitem_set.all(),
                         'order': order}
                return items

            except:

                []

        else:
            []


def updateItem(request):

    data= json.loads(request.body)
    productid= data['productId']
    action= data['action']

    user= request.user # returns the user requesting

    food_name = Restaurant.objects.get(id=productid) #this returns d food requested


    order, created = Order.objects.get_or_create(user=user, order_completed=False) #create or get a user order if it exixst by complete = False field

    orderItem, created= Orderitem.objects.get_or_create(order=order, food_name=food_name)
    print(orderItem.food_name.price)
    print(orderItem.quantity)
    print(orderItem.order)

    if action=='add':

        orderItem.quantity= (orderItem.quantity + 1)

    elif action == 'remove':
        orderItem.quantity = orderItem.quantity - 1

    orderItem.save()

    if orderItem.quantity <= 0:
        orderItem.delete()

    return JsonResponse('Item was added successfully', safe=False)
