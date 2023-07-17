#!/usr/bin/python3
"""
This is the Rectangle module
"""
from models.base import Base


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

    def area(self):
        """
        Returns the area of a rectangle instance
        """
        return self.__width * self.__height

    def display(self):
        """
        Prints in stdout the Rectangle instance whith
        the character #
        """
        rect = ""
        y_copy = self.__y

        for i in range(self.__height):
            if y_copy != 0:
                rect += ('\n' * y_copy)
                y_copy = 0
            x_copy = self.__x

            for j in range(self.__width):
                if x_copy != 0:
                    rect += (' ' * x_copy)
                    x_copy = 0
                rect += '#'

            if i == self.__height - 1:
                break
            else:
                rect += '\n'
        print(rect)

    def update(self, *args, **kwargs):
        """
        assigns an argument to each attribute
        """
        if len(args) != 0:
            if len(args) > 0:
                self.id = args[0]
            if len(args) > 1:
                self.__width = args[1]
            if len(args) > 2:
                self.__height = args[2]
            if len(args) > 3:
                self.__x = args[3]
            if len(args) > 4:
                self.__y = args[4]
        elif len(kwargs) != 0:
            for key, value in kwargs.items():
                if hasattr(self, key):
                    setattr(self, key, value)

    def __str__(self):
        """
        Returns a string representation
        """
        s1 = "[Rectangle] (" + str(self.id) + ") " + str(self.__x) + "/"
        s2 = str(self.__y) + " - " + str(self.__width) + "/"
        s3 = str(self.__height)
        s = s1 + s2 + s3
        return s

    def to_dictionary(self):
        """
        Returns the dictionary representation of a rectangle
        """
        _dict = {'x': self.__x, 'y': self.__y, 'id': self.id, 'height': self.__height, 'width': self.__width}
        return _dict
        return 
