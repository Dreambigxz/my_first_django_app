from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.views.generic import (View, TemplateView)
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import (Capital, Unpaid_user, Paid_user,
                     Payer_transaction_table,
                     Receivers_transaction_table)

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

            print('this is value', valu)

            if valu < 0:

                print('yes am less than 0')

                """
                 create receivers table and send mai
                 """

                receiver_transaction_table = Receivers_transaction_table.objects.create(receiver_details=receiver,
                                                                                        payer_details=payer,
                                                                                        amount_to_receive=payer.amount_to_pay)

                """
                receivers table created, now send mail
                """


                receiver.amount_merged += payer.amount_to_pay
                receiver.amount_to_merge = (-+valu)
                receiver.save()

################################################################################################################################


                """
                  create payers table and send mai
                """
                payer_transaction_details = Payer_transaction_table.objects.create(payer_details=payer,
                                                                                   receiver_details=receiver,
                                                                                   amount_to_pay=payer.amount_to_pay)
                """
                Table created, now send mail
                """

                payer.amount_merged += payer.amount_to_pay
                payer.amount_to_pay = 0.0
                payer.merged_to_pay = True
                payer.save()

                print('this is,', payer.user)


                print(paid)
                print(unpaid)


            else:


                print('no valu is greater than 0')

                print('this is,', payer.user)

                """
                create payers table and send mail
                """
                payer_transaction_details = Payer_transaction_table.objects.create(payer_details=payer,
                                                                                   receiver_details=receiver,
                                                                                   amount_to_pay=receiver.amount_to_merge)

                """
                 Table created, now send mail
                """

                payer.amount_merged += receiver.amount_to_merge
                payer.amount_to_pay = valu
                payer.save()

                if valu == 0.0:
                    payer.merged_to_pay = True
                    payer.save()

#################################################################################

                print('this is,', receiver.user)
                """
                 create receivers table and send mai
                 """

                amount = receiver.amount_to_merge
                receiver_transaction_table = Receivers_transaction_table.objects.create(receiver_details=receiver,
                                                                                        payer_details=payer,
                                                                                        amount_to_receive=receiver.amount_to_merge)

                """
                receivers table created, now send mail
                """

                receiver.amount_merged += receiver.amount_to_merge
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


