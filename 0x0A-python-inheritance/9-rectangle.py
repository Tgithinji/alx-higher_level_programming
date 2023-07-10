#!/usr/bin/python3
""" module representing a class Rectangle """

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Defines a class Rectangle that inherits from BaseGeometry
    """
    def __init__(self, width, height):
        """
        Initialize with a constructor
        """
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """
        returns an area of the rectangle
        """
        return self.__width * self.__height

    def __str__(self):
        """
        Returns a string representation
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
