#!/usr/bin/python3
import sys
t, res = 0, 0
while t < len(sys.argv):
    for arg in sys.argv[1:]:
        try:
            res += int(arg)
        except ValueError:
            # Ignore non-integer values
            pass
    t += 1
    break
print(res)
