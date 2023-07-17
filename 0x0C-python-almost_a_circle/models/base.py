#!/usr/bin/python3
"""
This is rhe base module
"""
import json
import os


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

    @classmethod
    def save_to_file(cls, list_objs):
        """
        writes the json string of list_objs to a file
        """
        if list_objs is None:
            list_objs = []

        filename = cls.__name__ + ".json"
        dict_list = [obj.to_dictionary() for obj in list_objs]
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(cls.to_json_string(dict_list))

    @staticmethod
    def from_json_string(json_string):
        """
        Returns a list from a json implementation
        """
        if json_string is None:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        Returns an instance with all attributes already set
        """
        if cls.__name__ == "Rectangle":
            obj = cls(2, 3)
        else:
            obj = cls(2)
        obj.update(**dictionary)
        return obj

    @classmethod
    def load_from_file(cls):
        """
        Returns a list of instances
        """
        filename = cls.__name__ + ".json"
        if os.path.exists(filename):
            with open(filename, 'r', encoding='utf-8') as f:
                json_str = f.read()
        list_dict = cls.from_json_string(json_str)
        return [cls.create(**obj) for obj in list_dict]
