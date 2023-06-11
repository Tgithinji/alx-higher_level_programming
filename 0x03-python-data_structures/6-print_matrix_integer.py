#!/usr/bin/python3

def print_matrix_integer(matrix=[]):
    for lst in matrix:
        for x in lst:
            if x == lst[-1]:
                print('{:d}'.format(x), end='')
            else:
                print('{:d}'.format(x), end=' ')
        print()
