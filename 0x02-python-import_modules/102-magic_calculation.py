#!/usr/bin/python3
def magic_calculation(a, b):
    add = None
    sub = None

    if a < b:
        from magic_calculation_102 import add, sub
        c = add(a, b)

        for i in range(4, 6):
            c = add(c, i)

        return c

    return sub(a, b)
