#!/usr/bin/python3
# Author - SAL

"""
Print the numbers from 1 to 100 separated by a space.
For multiples of three, print Fizz instead of the number
For multiples of five, print Buzz instead of the number.
For multiples of three and five, print FizzBuzz instead of the number.
"""

FIZZ = "Fizz"
BUZZ = "Buzz"

def fizzbuzz():
    for number in range(1, 101):
        if (number % 3 and number % 5):
            print("%s%s" % (FIZZ, BUZZ), end=' ')
        elif (number % 3):
            print("%s" % (FIZZ), end=' ')
        elif (number % 5):
            print("%s" % (BUZZ), end=' ')
        else:
            print("%d" % (number), end=' ')
