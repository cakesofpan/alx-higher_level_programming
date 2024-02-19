#!/usr/bin/python3
"""Defines an inherited list class MyList."""


class MyList(list):
    '''A class-level docstring'''
    def print_sorted(self):
        '''Prints sorted list'''
        print(sorted(self))
