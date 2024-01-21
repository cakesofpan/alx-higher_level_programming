#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    newl = []
    for x in my_list:
        if x % 2 == 0:
            newl.append(True)
        else:
            newl.append(False)
    return(newl)
