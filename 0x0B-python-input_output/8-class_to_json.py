#!/usr/bin/python3
"""
This module defines class_to_json function
"""


def class_to_json(obj):
    """
    Takes an object as input and
    Returns its dictionary description with simple data structures
    """
    return obj.__dict__
