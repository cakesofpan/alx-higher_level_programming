#!/usr/bin/python3
'''returns true if object is an instance of a specified class or
an instance of inherited class else false'''


def is_kind_of_class(obj, a_class):
    '''Check if an object is an instance or inherited instance of a class.

    Args:
        obj (any): The object to check.
        a_class (type): The class to match the type of obj to.
    '''
    if isinstance(obj, a_class):
        return True
    return False
