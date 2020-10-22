from .models import UserWallet
from users.myfunc import timestamp_Otp_Verification


def user_wallet(request):

    pass

    if request.user.is_anonymous:

        return {
            'user_balance': '0.00',
        }

    else:
        user_wallet=UserWallet.objects.filter(user=request.user)



        return  {
                'user_wallet': user_wallet,
                    }

def ref_deposit(request):

    if request.user.is_anonymous:

        return {
            'user_balance': '0.00',
        }
    else:
        deposit_ref = timestamp_Otp_Verification()

        return {
            'deposit_ref': deposit_ref
        }

