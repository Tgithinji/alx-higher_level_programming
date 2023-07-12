#!/usr/bin/python3
"""
Defines a class student
"""


class Student():
    """
    class student that creates an instance of a Student
    """
    def __init__(self, first_name, last_name, age):
        """
        initialize properties
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        retrieves a dictionary representation of an inatance
        """
        dct = {}
        if attrs is not None and isinstance(attrs, list):
            for item in attrs:
                if hasattr(self, item):
                    dct[item] = getattr(self, item)
            return dct
        else:
            return self.__dict__
