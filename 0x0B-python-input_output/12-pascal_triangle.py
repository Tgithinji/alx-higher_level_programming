#!/usr/bin/python3
"""
This module defines Pascal_triangle function
"""


def pascal_triangle(n):
    """
    Takes an integer n
    Returns a list of list of integers representing a     pascals triangle of n
    """
    lst = []

    if n <= 0:
        return lst
    for i in range(1, n+1):
        row=[]
        bin_c = 1
        for x in range(1, i+1):
            row.append(bin_c)
            bin_c = bin_c * (i - x) // x
        lst.append(row)
    return lst
