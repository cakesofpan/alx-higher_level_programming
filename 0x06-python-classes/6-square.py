#!/usr/bin/python3
class Square:
    '''This is a class-level docstring

    Writes an empty class Square that defines a square:
    '''

    def __init__(self, size=0, position=(0, 0)):
        '''This is a method-level docstring for the __init__ method.

        Args:
            size (int): length of a square
            position (int): a tuple
        '''
        self.__size = size
        self.__x, self.__y = position

    @property
    def position(self):
        return self.__x, self.__y

    @property
    def size(self):
        '''This is a method-level docstring for the size method. Retrieves data
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

    @position.setter
    def position(self, value):
        '''This is a method-level docstring for the position method. Sets it

        Args:
            value (int): a tuple
        '''
        if not isinstance(position, int):
            raise TypeError("position must be a tuple of 2 positive integers")

    def area(self):
        '''This is a method-level docstring for the area method.

        '''
        return self.__size**2

    def my_print(self):
        '''This is a method-level docstring for the my_print method. Prints a square with the character '#'

        '''
        if self.__size == 0:
            pass
        else:
            for t in range(self.__size):
                print(self.__x, self.__y)
                #print(self.__y)
                #print(tuples)
                for u in range(self.__size):
                    print("#", end="")

                    if u == self.__size:
                        print('\n')
