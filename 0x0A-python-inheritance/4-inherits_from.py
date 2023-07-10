#!/usr/bin/python3

"""
Defines a module that checks if object is an instance
of a class that inherited from the specific class
"""


def inherits_from(obj, a_class):
    """
    Returns True if check is true otherwise false
    """
    return issubclass(type(obj), a_class) and type(obj) is not a_class
