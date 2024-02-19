#!/usr/bin/python3
'''A module level docstring'''


def write_file(filename="", text=""):
    '''writes a string to a text file, returns no of chars written
    Args:
        filename (str): name of file
        text (str): string to be written to the file'''
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
