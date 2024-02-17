#!/usr/bin/python3
class Rectangle:
    '''This is a class-level docstring for class rectangle
    '''
    def __init__(self, width=0, height=0):
        '''This is a method-level docstring for __init__
        Args:
        width: (int) width of a rectangle
        height: (int) height of rectangle
        '''
        self.width = width
        self.height = height

    @property
    def width(self):
        '''This is a method_level docstring that retrieves width
        '''
        return self.__width

    @width.setter
    def width(self, value):
        '''This is a method_level docstring that sets width
        Args:
        value: (int) an integer
        '''
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        '''This is a method_level docstring that retrieves height
        '''
        return self.__height

    @height.setter
    def height(self, value):
        '''This is a method_level docstring that retrieves height
        Args:
        value: (int) an integer
        '''
        self.__height = value
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")

    def area(self):
        '''This is a method-level docstring that calculates area of a rectangle
        '''
        return self.__width * self.__height

    def perimeter(self):
        '''This is a method-level docstring calculates perimeter of rectangle
        '''
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return 2 * (self.__width + self.__height)
