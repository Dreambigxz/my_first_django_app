from django.shortcuts import (HttpResponse, redirect, render, resolve_url,
                              get_object_or_404, get_list_or_404, reverse,loader)

from django.views.generic.edit import View, CreateView, UpdateView, DeleteView

from .forms import ShippingAddressForm
from .models import ShippingAddress
from users.models import MyUser
from django.template.loader import render_to_string
from django.forms.models import model_to_dict
from django.http import JsonResponse
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

# from myproject.users.forms import UserChangeForm
from django.contrib.auth.forms import PasswordChangeForm

class UpdateShippingDetails(UpdateView):

    form_class = ShippingAddressForm
    model = ShippingAddress
    template_name = 'crud/edit_shipping_address.html'


class AccountDetails(UpdateView):

    model = MyUser
    template_name = 'ecomm/account.html'
    fields = ('username', 'full_name', 'email', 'phone_number')


class UpdateShippingAddress(View):

    def get(self, request, pk):


        shipping_adddress_update_key = get_object_or_404(ShippingAddress, pk=pk)
        print(shipping_adddress_update_key.pk)
        form= ShippingAddressForm(instance=shipping_adddress_update_key)
        html_form= render_to_string('crud/update_shipping_address.html', {'form':form, }, request=request)
        return JsonResponse({'html_form': html_form})


    def post(self, request, pk):


        data= dict()
        shipping_adddress_update_key = get_object_or_404(ShippingAddress, pk=pk)

        if request.is_ajax and request.method == 'POST':
            form= ShippingAddressForm(instance=shipping_adddress_update_key, data=request.POST)

            if form.is_valid():
                form.save()
                data['saved']= True

                messages.success(request, 'Address saved successfully')
                return JsonResponse(data)

        return redirect('account')

