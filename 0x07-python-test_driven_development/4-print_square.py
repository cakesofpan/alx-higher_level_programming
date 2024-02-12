#!/usr/bin/python3
def print_square(size):
	'''This is a method-level docstring that prints a square with #'''
	if not isinstance(size, int):
		raise TypeError("size must be an integer")
	if size < 0:
		raise ValueError("size must be >= 0")

	s, t = 0, 0
	for s in range(size):
		for t in range(size):
			print('#', end="")
		print()
