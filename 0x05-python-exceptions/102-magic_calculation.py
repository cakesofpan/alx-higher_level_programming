#!/usr/bin/python3
def magic_calculation(a, b):
    final = 0

    for t in range(1, 4):
        try:
            if t > a:
                raise Exception('Too far')
            final += (a ** b) / t
        except:
            final += b + a
            break

    return final
