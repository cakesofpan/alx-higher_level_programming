#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        res = fct(*args)
        return res
    except Exception as ex:
        print("Exception:", ex, file=sys.stderr)
        return None
