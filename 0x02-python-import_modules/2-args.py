#!/usr/bin/python3
import sys
num = len(sys.argv) - 1
t = 1
if num == 0:
    print(f"{num} argument{'s' if num != 1 else ''}.")
else:
    print(f"{num} argument{':' if num == 1 else 's:'}")
    while t < (num + 1):
        print(f"{t}: {sys.argv[t]}")
        t += 1
