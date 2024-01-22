#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    try:
        for t in range(x):
            value = my_list[t]
            if type(value) == int:
                print("{:d}".format(value), end=" ")
                count += 1
    except IndexError:
        pass
    return count
