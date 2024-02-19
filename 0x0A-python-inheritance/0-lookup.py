#!/usr/bin/python3
'''Defines an attribute lookup function'''


def lookup(obj):
    '''returns the list of available attributes and methods of an object
    Args:
        obj (any): object to be checked
    '''
    return (dir(obj))
