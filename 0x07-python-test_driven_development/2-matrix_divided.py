#!/usr/bin/python3
def matrix_divided(matrix, div):
	t = 0
	new_matrix = []
	row_size = len(matrix[0])

	if not isinstance(div, (int, float)):
		raise TypeError("div must be a number")
	if div == 0:
		raise ZeroDivisionError("division by zero")

	for row in matrix:
		if row_size != len(row):
			raise TypeError("Each row of the matrix must have the same size")
		new_row = []
		for t in row:
			if not isinstance(t, (int, float)):
				raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
			new_row.append(round(t / div, 2))
		new_matrix.append(new_row)
	return(new_matrix)
