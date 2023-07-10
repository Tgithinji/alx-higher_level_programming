#!/usr/bin/python3

"""
This module checks if the object is an instance of,
or if the object is an instance of a class that
inherited from a specific class
"""


def is_kind_of_class(obj, a_class):
    """
    Return True if the check is true and False otherwise
    """
    return isinstance(obj, a_class)
