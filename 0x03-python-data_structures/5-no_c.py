#!/usr/bin/python3
def no_c(my_string):
    res = ""

    for x in my_string:
        if x.lower() not in ['c'] or x.upper() not in ['C']:
            res += x
    return (res)
