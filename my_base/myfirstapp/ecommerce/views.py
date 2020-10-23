from django.shortcuts import (render,
                              HttpResponse,
                              reverse,
                              get_object_or_404, redirect)

from django.contrib import messages
from django.views.generic import TemplateView, ListView, DetailView, View, CreateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.messages.views import SuccessMessageMixin
from .models import Products, Order, Orderitem, ShippingAddress, Rating, ProductReviews
import random
import json
from django.core.exceptions import ValidationError
from users.models import MyUser
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.contrib.auth import update_session_auth_hash
from .forms import ShippingAddressForm

from django.db.models import Q
from userwallet.models import UserWallet
from django.core import serializers
from ast import literal_eval

from rave_python import Rave, RaveExceptions, Misc
from django.db.models import Max
from django.db.models import Count
from django.db.models import F
import uuid


def session_id():
    return (uuid.uuid4().hex[:20])


# Create your views here.


####GLOBAL VARIBLES ###########


################## Pages ###########

class HomeListView(ListView):
    # model =  Products
    context_object_name = 'products'
    template_name = 'ecomm/home.html'
    ordering = ('-rating__rated')

    def get_queryset(self):

        pass

    def get_context_data(self, *, object_list=None, **kwargs):

        context = super(HomeListView, self).get_context_data(**kwargs)

        try:
            device = self.request.COOKIES['device']

        except:
            device = {}

        price_total = ([i.item.price * i.quantity for i in Orderitem.objects.filter(device_name=device)])
        orderitem = Orderitem.objects.filter(device_name=device, )
        context['item'] = orderitem
        context['price_total'] = sum(price_total)

        # context['userwallet']=UserWallet.objects.filter(user=self.request.user)

        context['products'] = {'women': Products.objects.filter(Cartegory='Womens'),
                               'top_10': Products.objects.filter(Cartegory='Top_10').order_by(),
                               'tele': Products.objects.filter(Cartegory='Televisons'),
                               }

        return context


class ProductDetailView(DetailView):
    template_name = 'ecomm/product-details.html'
    model = Products

    def get_context_data(self, **kwargs, ):
        context = super(ProductDetailView, self).get_context_data(**kwargs)

        obj = kwargs

        product = (obj['object'])
        get_product = Products.objects.get(product_name=product)

        cartegory = get_product.Cartegory

        get_related_product = Products.objects.filter(Cartegory=cartegory)
        context['related_product'] = get_related_product

        print(get_related_product)

        return context


class CartListView(SuccessMessageMixin, ListView):
    template_name = 'ecomm/cart.html'
    context_object_name = 'cart'

    def get_queryset(self):
        return Orderitem.objects.all()

    def get_context_data(self, *, object_list=None, **kwargs):

        try:
            device = self.request.COOKIES['device']

        except:
            device = {}


        orderitem = Orderitem.objects.filter(device_name=device)

        # orderitem = Orderitem.objects.filter(device_name=device, )

        item_total = ([i.quantity for i in Orderitem.objects.filter(device_name=device)])
        price_total = ([i.item.price * i.quantity for i in Orderitem.objects.filter(device_name=device)])

        context = super(CartListView, self).get_context_data(**kwargs)

        context['orderitem'] = orderitem
        context['item_total'] = sum(item_total)
        context['price_total'] = sum(price_total)

        print(context['orderitem'])

        return context


class CheckOutListView(LoginRequiredMixin, SuccessMessageMixin, ListView):
    login_url = 'login'
    redirect_field_name = 'checkout'
    template_name = 'ecomm/checkout.html'
    context_object_name = 'check_out'
    form_class = ShippingAddressForm
    initial = {'key': 'value'}

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Orderitem.objects.all()

    def get_context_data(self, **kwargs):

        if self.request.user.is_authenticated:

            device = self.request.COOKIES['device']

            generate_random_num = (random.randint(45995, 67995))
            orderitem = Orderitem.objects.filter(Q(user=self.request.user) | Q(device_name=device))
            # orderitem = Orderitem.objects.filter(user=self.request.user)
            item_total = ([i.quantity for i in Orderitem.objects.filter(user=self.request.user)])
            price_total = ([i.item.price * i.quantity for i in Orderitem.objects.filter(user=self.request.user)])

            context = super(CheckOutListView, self).get_context_data(**kwargs)
            context['cart'] = orderitem
            context['item_total'] = sum(item_total)
            context['price_total'] = sum(price_total, 500)
            context['txref_random'] = generate_random_num

            if ShippingAddress.objects.filter(myuser=self.request.user).exists():
                pass
            else:
                context['forms'] = self.form_class

            context['user_shipping_details'] = ShippingAddress.objects.filter(myuser=self.request.user)

            return context
        else:
            []

    def post(self, request, *args, **kwargs):

        data = dict()

        form = self.form_class(data=request.POST)
        if form.is_valid():
            # get the current user
            user = self.request.user

            user_form = form.save(commit=False)

            user_form.myuser = user
            user_form.save()

            data['saved'] = True

            return JsonResponse(data, status=200)


################## USER PROCESSING ITEM LOGIC ###########

def AddtoCart(request, slug, ):
    product = get_object_or_404(Products, slug=slug)

    # get_list=[]
    # if request.is_ajax and request.method== 'GET':
    #     get_the_user_color= request.GET.get('color')
    #     print(list(get_the_user_color))

    data = dict()

    device = request.COOKIES['device']

    # use product to create orderitem

    create_orderitem_table, created = Orderitem.objects.get_or_create(device_name=device, item=product)

    order_exist = Orderitem.objects.filter(device_name=device, item__product_name=create_orderitem_table)

    if order_exist.exists():
        create_orderitem_table.quantity += 1
        item_added = create_orderitem_table.save()

        response = redirect('product_store')  # replace redirect with HttpResponse or render
        response.set_cookie('cookie_name', 'cookie_value', max_age=1000)

        cart_total = ([i.quantity for i in Orderitem.objects.filter(device_name=device)])

        item_total = ([i.quantity for i in Orderitem.objects.filter(device_name=device, item=product)])
        price_total = ([i.item.price * i.quantity for i in Orderitem.objects.filter(device_name=device, item=product)])
        grand_total = ([i.item.price * i.quantity for i in Orderitem.objects.filter(device_name=device)])

        if create_orderitem_table.quantity == 1:
            data['added'] = True, sum(cart_total), create_orderitem_table.item.product_name
            return JsonResponse(data)

        else:
            if request.is_ajax:
                data['inc'] = True, sum(cart_total), create_orderitem_table.item.product_name, sum(
                    grand_total), price_total, sum(item_total)
                return JsonResponse(data)


def ClearCart(request):
    device = request.COOKIES['device']

    items = Orderitem.objects.filter(device_name=device)

    items.delete()

    messages.success(request, 'You cleared Your cart')
    return redirect('cart')


def IncreaseQty(request, slug):
    device = request.COOKIES['device']
    items = Orderitem.objects.filter(user=request.user, item__slug=slug)

    for i in items:
        i.quantity += 1
        i.save()

    messages.success(request, "{} Increased by one".format(i.item))
    return redirect('cart')

    # return redirect('cart')


def DecreaseQty(request, slug):
    device = request.COOKIES['device']
    product = get_object_or_404(Products, slug=slug)

    items = Orderitem.objects.filter(device_name=device, item=product)

    data = dict()
    for i in items:

        if request.is_ajax:

            if i.quantity == 1:

                data['valu'] = 1

                return JsonResponse(data)

            else:

                i.quantity -= 1
                i.save()

                item_total = ([i.quantity for i in Orderitem.objects.filter(device_name=device, item=product)])
                cart_total = ([i.quantity for i in Orderitem.objects.filter(device_name=device)])
                price_total = (
                [i.item.price * i.quantity for i in Orderitem.objects.filter(device_name=device, item=product)])
                grand_total = ([i.item.price * i.quantity for i in Orderitem.objects.filter(device_name=device)])
                get_product = product.product_name

                data['sub'] = True, sum(cart_total), sum(grand_total), price_total, item_total, get_product
                return JsonResponse(data, status=200)


def deleteanitem(request, slug):
    device = request.COOKIES['device']

    items = Orderitem.objects.filter(device_name=device, item__slug=slug)

    items.delete()
    return redirect('cart')


def payment(request):
    data = json.loads(request.body)
    ref_id = data['data']
    device = request.COOKIES['device']


    print(ref_id)

    print(ref_id['amount'])

    rave = Rave("PK", "SK")
                usingEnv=False)

    verify_payment = rave.Card.verify(ref_id['tx_ref'])
    order_id = verify_payment['txRef']
    payment_ref = verify_payment['flwRef']
    print(verify_payment)

    if verify_payment['chargecode'] == '00' and verify_payment['amount'] == verify_payment['chargedamount'] and \
            verify_payment['error'] == False:

            # if amount paid is == to amounnt charged, create an order with the orderitem and clear a users cart

            generate_random_num_for_order_id = (random.randint(45995, 67995))

                # get all the user item in the cart
            orderitems = Orderitem.objects.filter(device_name=device)



            # iterate and create an order table with the user item in cart

            # create_order = Order(myuser=request.user,)
            for orders in orderitems:

                orders.user= request.user
                orders.save()

                # create an order with the item in their cart
                order = Order.objects.create(myuser=orders.user, orderitem=orders.item, user_quantity=orders.quantity,
                                            order_id = ('GS' + str(order_id)), reference_id = payment_ref, ordered = True,
                                             total=orders.get_price())


                # order created succesffull   y

                # delete user cart from database
                orderitems.delete()

                return redirect('/')


class Account(LoginRequiredMixin, View):
    login_url = '/login/'
    redirect_field_name = 'login'
    form_class = ShippingAddressForm

    def get(self, request, ):

        # get the user ordered item
        user_order = Order.objects.filter(myuser=self.request.user)

        # shipping address

        shipping_address = ShippingAddress.objects.filter(myuser=self.request.user)

        user_profile = self.request.user
        print(self.form_class)

        return render(request, 'ecomm/my-account.html', {'order': user_order,
                                                         'shipping_address': shipping_address,
                                                         'user_profile': user_profile, 'forms': self.form_class})

    def post(self, request, *args, **kwargs):

        if request.method == 'POST':

            fullname = request.POST.get('full-name')
            username = request.POST.get('username')
            number = request.POST.get('number')
            current_pwd = request.POST.get('current-pwd')
            new_pwd = request.POST.get('new-pwd')
            confirm_pwd = request.POST.get('confirm-pwd')

            print(fullname, '\n', username, '\n', number, '\n', current_pwd,
                  '\n', new_pwd, '\n', confirm_pwd)

            user = (self.request.user)
            user.full_name = fullname
            user.username = username
            user.phone_number = number

            if confirm_pwd == '':

                user.save()
                messages.success(request, 'Account updated Successfully', extra_tags='success')

            else:

                if ((user.check_password(current_pwd))):

                    if new_pwd == confirm_pwd:

                        user.set_password(new_pwd)
                        user.save()
                        update_session_auth_hash(self.request, user)
                        messages.success(request, 'Account updated Syuccessfully')
                    else:
                        PASSMIS = 50
                        messages.add_message(request, PASSMIS, 'Password Missmatch')

                else:
                    messages.error(request, 'Old password not correct')

            return redirect('account')


class RatingViews(DetailView):
    model = Products
    template_name = 'ecomm/rate.html'


def RAtingProcess(request, slug):
    if request.is_ajax and request.method == 'GET':
        rating = request.GET.get('data')
        divide_rating = int(rating)

    product = get_object_or_404(Products, slug=slug)
    user = request.user

    if Rating.objects.filter(user=request.user, product=product).exists():
        print('This user has rated this product')
        return redirect('product', slug=slug)

    else:

        if ProductReviews.objects.filter(user=request.user, product=product).exists():

            print(True)

            update_user_reviews_rating = ProductReviews.objects.filter(user=request.user, product=product)

            for r in update_user_reviews_rating:
                print(r.rating)
                r.rating = rating
                r.save()
                rating = Rating.objects.create(user=user, rated=rating, product=product)

        else:

            rating = Rating.objects.create(user=user, rated=rating, product=product)
            print(False)

    return redirect('/')


def ProcessReviews(request, slug):
    if request.method == 'POST' and request.user.is_authenticated:
        user_review = request.POST.get('review')
        print(user_review)

        product = get_object_or_404(Products, slug=slug)

        if ProductReviews.objects.filter(user=request.user, product=product).exists():

            messages.success(request,
                             'Hello {} you cant add more than one review on one product'.format(request.user.username))
            print('This user has rated this product')
            return redirect('product', slug=slug)


        else:

            if Rating.objects.filter(user=request.user, product=product).exists():

                print(True)

                rate = Rating.objects.filter(user=request.user, product=product)

                for r in rate:
                    save_user_review = ProductReviews.objects.get_or_create(user=request.user, product=product,
                                                                            your_review=user_review, rating=r.rated)

                    messages.success(request, 'Review updated successfully')
                    return redirect('product', slug=slug)

            else:
                save_user_review = ProductReviews.objects.get_or_create(user=request.user, product=product,
                                                                        your_review=user_review)

                messages.success(request, 'Review updated successfully')
                return redirect('product', slug=slug)
    else:
        return redirect('login')
