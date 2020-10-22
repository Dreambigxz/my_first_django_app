from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.views.generic import (View, TemplateView)
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Capital, Unpaid_user, Paid_user

# Create your views here.

class HomeView(TemplateView):

    template_name = 'trade/home.html'


class UserDashboard(LoginRequiredMixin, View):
    login_url = 'sign_in'


def get(self, request):
    # get paid and unpaid users

    paid = Paid_user.objects.filter(merged_to_receive=False)
    unpaid = Unpaid_user.objects.filter(merged_to_pay=False)

    print(unpaid)
    print(paid)

    # ussing while loop for mergig
    while paid.count() != 0 and unpaid.count() != 0:

        receiver = paid[0]
        payer = unpaid[0]

        print(receiver)
        print(payer)

        valu = payer.amount_to_pay - receiver.amount_to_merge

        print(valu)

        if valu < 0:

            print('yes am less than 0')

            receiver.amount_merged += payer.amount_to_pay
            receiver.amount_to_merge = (-+valu)
            receiver.save()

            #########create receivers table and dispatch mail################

            user = payer.user
            receivers_id = receiver.id
            amount = payer.amount_to_pay

            payer.amount_merged += payer.amount_to_pay
            payer.amount_to_pay = 0.0
            payer.merged_to_pay = True
            payer.save()

            print(paid)
            print(unpaid)

            #########create payers transaction table and dispatch mail ################

            payer_transaction_table = PTransaction.objects.create(user=user, receivers_id=receivers_id, amount=amount)

            break
        else:
            print('no valu is greater than 0')

            payer.amount_merged += receiver.amount_to_merge
            payer.amount_to_pay = valu
            payer.save()

            if valu == 0.0:
                payer.merged_to_pay = True
                payer.save()

            receiver.amount_merged += receiver.amount_to_receive
            receiver.amount_to_merge = 0.0
            receiver.merged_to_receive = True
            receiver.save()

            print(paid)
            print(unpaid)
    return render(request, 'dashboard/dashboard.html')


class UserTransactions(View):
    def get(self, request):

        return render(request, 'dashboard/transactions.html')


class UserAccount(View):
    def get(self, request):
        return render(request, 'dashboard/accounts.html')


class UserSettings(View):

    def get(self, request):
        return render(request, 'dashboard/settings.html')


