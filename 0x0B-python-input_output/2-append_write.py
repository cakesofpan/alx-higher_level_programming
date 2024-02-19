#!/usr/bin/python3
'''A module level docstring'''


def write_file(filename="", text=""):
    '''appends a string to a text file, returns no of chars added
    Args:
        filename (str): name of file
        text (str): string to be written to the file'''
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
