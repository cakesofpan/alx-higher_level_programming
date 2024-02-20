#!/usr/bin/python3
'''A module-level docstring that creates a class based on the previous file '''


class BaseGeometry
    '''represents base geometry'''
    def area(self):
        '''Raises an exception'''
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        '''Validate a parameter as an integer.

        Args:
            name (str): The name of the parameter.
            value (int): The parameter to validate.
        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is <= 0.
        '''
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
