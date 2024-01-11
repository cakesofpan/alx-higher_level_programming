#!/usr/bin/python3
for t in range(0, 100):
    if t < 10:
        t = '0' + str(t)

    t = str(t)
    if t[0] > t[1] or t[0] == t[1]:
        continue

    if t == 89:
        print(t)
    else:
        print("{}, ".format(t), end="")
