#!/usr/bin/python3
'''A module level docstring'''


def read_file(filename=""):
    '''reads a text file and prints to stdout
    Args:
        filename (str): name of file '''
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
