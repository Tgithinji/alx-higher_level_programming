#!/usr/bin/python3
"""
This is rhe base module
"""
import json


class Base():
    """
    This creates instances of class Base
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initilizes instances of Base
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Returns the JSON string representation oflist_dictionaries
        """
        if list_dictionaries is None:
            return "[]"
        else:
            return json.dumps(list_dictionaries)
