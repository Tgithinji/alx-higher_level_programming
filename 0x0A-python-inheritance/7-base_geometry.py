#!/usr/bin/python3

"""
a class BaseGeometry based on module 6-base_geometry.py
"""


class BaseGeometry():
    """
    Defines  the class BaseGeometry
    """
    def area(self):
        """
        raises an exception
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        validates value
        """
        if type(value) is not int:
            message = name + " must be an integer"
            raise TypeError(message)
        if value <= 0:
            message = name + " must be greater than 0"
            raise ValueError(message)
