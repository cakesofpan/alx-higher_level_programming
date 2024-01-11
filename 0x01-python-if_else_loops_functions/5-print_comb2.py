#!/usr/bin/python3
for t in range(0, 100):
    if t < 10:
        t = '0' + str(t)
    if t != 99:
        print("{}, ".format(t), end="")
    else:
        print(t)
