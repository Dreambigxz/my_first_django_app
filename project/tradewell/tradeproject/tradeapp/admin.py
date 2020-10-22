from django.contrib import admin
from .models import Capital, Unpaid_user, Paid_user, Receivers_transaction_table, Payer_transaction_table

# Register your models here.
admin.site.register(Capital)
admin.site.register(Unpaid_user)
admin.site.register(Paid_user)
admin.site.register(Receivers_transaction_table)
admin.site.register(Payer_transaction_table)