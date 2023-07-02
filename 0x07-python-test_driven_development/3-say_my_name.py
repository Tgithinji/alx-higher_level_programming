#!/usr/bin/python3

"""
say_my_name module prints a string
first_name: a string
last_name: a string
"""


def say_my_name(first_name, last_name=""):
    """
    prints a string of names
    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
