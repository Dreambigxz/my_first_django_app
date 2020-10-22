import random

import calendar;
import time;
ts = calendar.timegm(time.gmtime())


# using list comprehension
# to convert number to list of integers
res = [int(x) for x in str(ts)]
last_5_digit= (res[6:])

account_number= (res[3:])

def convert(list):
    # Converting integer list to string list
    s = [str(i) for i in list]

    # Join list items using join()
    res = int("".join(s))
    return (res)


def otp_Verification():

    list = last_5_digit
    token_convert=(convert(list))
    radnum= (random.randint(token_convert, 774241))

    return radnum   # print(ts)


def account_number_generator():

    list = account_number
    account_number_convert=(convert(list))
    radnum = (random.randint(1130665, 7742415))
    user_account_number = '771' + str(radnum)
    return user_account_number


print(account_number_generator())
print(otp_Verification())