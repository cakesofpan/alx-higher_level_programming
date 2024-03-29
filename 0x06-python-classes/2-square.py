#!/usr/bin/python3
'''This is a module level docstring for 2-square
'''


class Square:
    '''This is a class-level docstring

    Writes an empty class Square that defines a square:
    '''

    def __init__(self, size=0):
        '''This is a method-level docstring for the __init__ method.

        Args:
            size (int): length of the square
        '''
        try:
            if size < 0:
                raise ValueError
            if not isinstance(size, int):
                raise TypeError

            self.__size = size
        except TypeError:
            print("size must be an integer")

        except ValueError:
            print("size must be >= 0")
