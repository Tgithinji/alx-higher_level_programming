#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    new_matrix = []
    for x in matrix:
        mtrx = list(map(lambda v: v * v, x))
        new_matrix.append(mtrx)
    return new_matrix
