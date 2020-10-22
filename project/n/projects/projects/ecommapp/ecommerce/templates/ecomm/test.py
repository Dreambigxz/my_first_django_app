# success_data={
#
# 'error': False,
# 'transactionComplete': True,
# 'txRef': '58028',
#  'flwRef': 'FLW-MOCK-5b57599bac5f957abdf34cf9bc9d8824',
#  'amount': 600, 'chargedamount': 600, 'cardToken': 'flw-t1nf-cc8b5c30a5563f637eb83dac1bab20df-m03k',
#   'vbvmessage': 'Approved. Successful',
#    'chargemessage': 'Please enter the OTP sent to your mobile number 080****** and email te**@rave**.com',
#    'chargecode': '00', 'currency': 'NGN'
#    }


d = {'dict1': {'qyantity': 233}, 'dict2': {'qyantity': 3}}


def fun():
 for k1, v1 in d.items():  # the basic way
 #  temp = ""
 #  temp += k1
 #  for k2, v2 in v1.items():
 #   temp = temp + " " + str(k2) + " " + str(v2)
 #   print(list(temp))

  yield  (sum(v1.values()))

# print(fun())

x= [i for i in fun()]

print(sum(x))