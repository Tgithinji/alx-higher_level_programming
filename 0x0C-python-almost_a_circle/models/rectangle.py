#!/usr/bin/python3
"""
This is the Rectangle module
"""
from  models.base import Base


class Rectangle(Base):
    """
    Defines a Rectangle class
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        initialize an instance
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """
        gets the value of width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        sets the value of width
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """
        Gets the value of height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        sets the height
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """
        retrives value of x
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        Sets the value of x
        """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """
        retrives value of y
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        Sets the value of y
        """
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value
