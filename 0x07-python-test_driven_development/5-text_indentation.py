#!/usr/bin/python3

"""
This module prints a text with two lines after some characters
param text: a string
"""


def text_indentation(text):
    """
    prints a text with two new lines after each provided delimiter
    """
    delims = ['.', '?', ':']
    delim_found = False
    if type(text) is not str:
        raise TypeError("text must be a string")

    for ch in text:
        if delim_found and ch == " ":
            delim_found = False
            continue
        if ch in delims:
            print("{}\n".format(ch))
            delim_found = True
        else:
            print(ch, end="")
