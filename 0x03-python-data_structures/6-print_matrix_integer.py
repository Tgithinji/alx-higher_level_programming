#!/usr/bin/python3

def print_matrix_integer(matrix=[]):
    if matrix is None:
        return
    for lst in matrix:
        for x in lst:
            print('{:d}'.format(x), end=' ')
        print('')
