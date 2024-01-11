#!/usr/bin/python3
def islower(c):
    c = ord(c)
    if c >= ord('a') and c <= ord('z'):
        return True

    elif c >= ord('0') and c <= ord('Z'):
        return False
