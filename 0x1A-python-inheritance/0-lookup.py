#!/usr/bin/python3

"""
defines a lookup function that looks up available
attributes and methods of an object
obj: the object
"""


def lookup(obj):
    """
    Returns a list object
    """
    return dir(obj)
