#!/usr/bin/python3
import random
number = random.randint(-10, 10)
if number > 0:
    print("%s is positive" % (number))
elif number == 0:
    print("%s is zero" % (number))
else:
    print("%s is negative" % (number))
