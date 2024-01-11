#!/usr/bin/python3
def print_last_digit(number):
    if (number < 0):
        number = -number

    if (number == 0):
        print("00")
    digit = number % 10
    return digit
