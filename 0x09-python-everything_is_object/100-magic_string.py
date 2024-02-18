#!/usr/bin/python3
def magic_string():
    return "BestSchool" * (1 + magic_string.count)
magic_string.count = 0
