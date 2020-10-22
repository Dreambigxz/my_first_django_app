from django.shortcuts import render, redirect, reverse
from django.views.generic import View, TemplateView
from .models import UserWallet
import json

from rave_python import Rave, RaveExceptions, Misc

# Create your views here.

class UserWalletViews(View):

    def get(self, request, *args, **kwargs):

        return render(request, 'wallet/my-wallet.html')


class Deposit(View):

    def post(self, request, *args, **kwargs):
        data = json.loads(request.body)
        deposit_status = data['data']

        print(deposit_status)

        print(deposit_status['amount'])

        rave = Rave("FLWPUBK_TEST-ad745b9b6ef96bf9f1b2834ac7fbc73a-X",
                    'FLWSECK_TEST-a8e4e10033ed523390c9f839d2214509-X',
                    usingEnv=False)

        verify_deposit_id = rave.Card.verify(deposit_status['tx_ref'])
        # order_id = verify_payment['txRef']
        # payment_ref = verify_payment['flwRef']
        print(verify_deposit_id)

        #get the user deposited amount and charged amount for proper check before crediting a user
        deposited_amount=verify_deposit_id['chargedamount']
        charged_amount=verify_deposit_id['amount']



        if deposited_amount == charged_amount:

            #get the user table and add the amount deposited

            userwallet= UserWallet.objects.filter(user=self.request.user)
            for userwallet in userwallet:
                userwallet.balance += charged_amount
                userwallet.save()

        return redirect('/')

