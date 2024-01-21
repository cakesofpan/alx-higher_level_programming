#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    newlist = my_list.copy()
    rep = newlist[idx] = element
    if idx < 0 or idx > len(my_list):
        return(my_list)
    else:
        return(newlist)
