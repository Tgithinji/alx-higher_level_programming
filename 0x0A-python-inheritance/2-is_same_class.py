#!/usr/bin/python3

"""
Define is_same_class module that checks if an object
is an instance of the specified class
obj: an object
a_class: a class
"""


def is_same_class(obj, a_class):
    """
    Returns true if obj is exact instance of a_class
    """
    return isinstance(obj, a_class)
