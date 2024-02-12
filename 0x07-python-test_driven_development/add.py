#!/usr/bin/python3
def add_integer(a, b=98):
	'''This is a method-level docstring for method add_integer
		just adds two integers
	'''
	if not (isinstance(a, int) or isinstance(a, float)):
		raise TypeError("a must be an integer")
	if not (isinstance(b, int) or isinstance(b, float)):
		raise TypeError("b must be an integer")

	return int(a) + int(b)
