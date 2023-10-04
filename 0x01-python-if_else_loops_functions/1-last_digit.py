#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number >= 0:
    lst_digit = number % 10
else:
    lst_digit = ((-number % 10) * -1)
message = f"Last digit of {number} is {lst_digit}"
if lst_digit == 0:
    print(f"%s and is 0" % (message))
elif lst_digit > 5 and lst_digit % 10 != 0:
    print(f"%s and is greater than 5" % (message))
else:
    print(f"%s and is less than 6 and not 0" % (message))
