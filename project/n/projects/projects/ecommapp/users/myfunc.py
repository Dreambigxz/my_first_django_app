# lst = range(344 ,5)
# # num = int(input('How many numbers: '))
# # for n in range(6):
# #     numbers = int(input('Enter number '))
# #     lst.append(numbers)
# # print("Sum of elements in given list is :", sum(lst))
#
# # val=map(int, str(lst))
# # print(sum(val))
#
# print(sum(lst))

import random

import calendar;
import time;
ts = calendar.timegm(time.gmtime())


# using list comprehension
# to convert number to list of integers
res = [int(x) for x in str(ts)]
last_5_digit= (res[6:])

account_number= (res[3:])

# print(account_number)


def convert(list):
    # Converting integer list to string list
    s = [str(i) for i in list]

    # Join list items using join()
    res = int("".join(s))
    return (res)


def timestamp_Otp_Verification():

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
print(timestamp_Otp_Verification())





# import datetime
# date_string = '2017-12-31'
# date_format = '%Y-%m-%d'
#
# try:
#   date_obj = datetime.datetime.strptime(date_string, date_format)
#   print(date_obj)
# except ValueError:
#   print("Incorrect data format, should be YYYY-MM-DD")