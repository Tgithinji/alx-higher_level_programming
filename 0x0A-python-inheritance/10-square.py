#!/usr/bin/python3
""" module that defines a square """
BaseGeometry = __import__('7-base_geometry').BaseGeometry
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """
    Defines a class Square that inherits from Rectangle
    """
    def __init__(self, size):
        """
        Initialize using a constructor
        """
        super().integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
