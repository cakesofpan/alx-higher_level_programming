#!/usr/bin/python3
'''This is a module level docstring for 4-square
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
        self.__size = size

    @property
    def size(self):
        '''This is a method-level docstring for the size method.Retrieves data
        '''
        return self.__size

    @size.setter
    def size(self, value):
        '''This is a method-level docstring for the size method.

        Args:
            value: length of the square
            '''
        try:
            if value < 0:
                raise ValueError
            if not isinstance(value, int):
                raise TypeError

            self.__size = value
        except TypeError:
            print("size must be an integer")

        except ValueError:
            print("size must be >= 0")

    def area(self):
        '''This is a method-level docstring for the area method.

        '''
        return self.__size**2
