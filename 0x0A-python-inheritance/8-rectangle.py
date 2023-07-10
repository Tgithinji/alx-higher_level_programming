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


"""
A child class Rectangle
"""


class Rectangle(BaseGeometry):
    """
    Defines a class Rectangle that inherits from BaseGeometry
    """
    def __init__(self, width, height):
        """
        Initialize with a constructor
        """
        self.__width = width
        self.__height = height
        super().integer_validator("width", self.__width)
        super().integer_validator("height", self.__height)
