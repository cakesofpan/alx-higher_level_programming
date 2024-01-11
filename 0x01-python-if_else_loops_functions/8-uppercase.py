#!/usr/bin/python3
def uppercase(str):
    res = ""
    for char in str:
        if 'a' <= char <= 'z':
            res += "{}".format(chr(ord(char) - ord('a') + ord('A')))
        else:
            res += char
    print(res)
