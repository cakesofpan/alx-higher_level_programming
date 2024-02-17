#!/usr/bin/python3
'''This is a module level docstring for 5-square
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
        '''This is a method-level docstring for the size method. Retrieves data
        '''
        return self.__size

    @size.setter
    def size(self, value):
        '''This is a method-level docstring for the size method. Sets it

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
        Calculates area of a square

        '''
        return self.__size**2

    def my_print(self):
        '''This is a method-level docstring for the my_print method.
        Prints a square with the character '#'

        '''
        if self.__size == 0:
            pass
        else:
            for t in range(self.__size):
                for u in range(self.__size):
                    print("#", end="")
                print('\n')
