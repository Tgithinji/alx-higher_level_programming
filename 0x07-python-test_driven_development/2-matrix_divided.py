#!/usr/bin/python3

"""
matrix_divided function takes a matrix and divides each integer by div
param matrix: a list of nested lists
param div: an integer to be divided by each number in matrix
"""


def matrix_divided(matrix, div):
    """
    Returns a new matrix
	"""
    if not matrix or matrix is None or matrix is [[]]:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = []
    for lst in matrix:
        nested_list = []
        if len(matrix[0]) != len(lst):
            raise TypeError("Each row of the matrix must have the same size")
        for x in lst:
            if type(x) is not int and type(x) is not float:
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
            else:
            	y = round((x / div), 2)
            	nested_list.append(y)
        new_matrix.append(nested_list)
    return new_matrix
