#!/usr/bin/python3

"""
add_attribute function adds a new attribute to an object
"""


def add_attribute(obj, name, value):
    """
    adds a new attribute to an object
    """
    if not isinstance(obj, (list, tuple, str, int)):
        setattr(obj, name, value)
    else:
        raise TypeError("can't add new attribute")
