#!/usr/bin/python3

"""
This module adds two integers or float together
param a: integer or float
param b: integer or float
"""


def add_integer(a, b=98):
    """
    Returns a + b, an integer
    """
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")

    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)

    return a + b

