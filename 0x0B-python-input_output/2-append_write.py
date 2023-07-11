#!/usr/bin/python3

"""
This module defines the append_write function
"""


def append_write(filename="", text=""):
    """
    This function appends a string at the end of a file
    Returns the number of characters added
    """
    with open(filename, 'a', encoding='utf-8') as f:
        return f.write(text)
