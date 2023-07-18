#!/usr/bin/python3
"""
This is rhe base module
"""
import json
import os
import csv
import turtle


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
        else:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
        serializes in cvs
        """
        filename = cls.__name__ + ".csv"
        if list_objs is None:
            list_objs = []
        dict_list = [obj.to_dictionary() for obj in list_objs]
        if cls.__name__ == "Rectangle":
            fieldnames = ['id', 'width', 'height', 'x', 'y']
        else:
            fieldnames = ['id', 'size', 'x', 'y']

        with open(filename, 'w', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            for dictionary in dict_list:
                writer.writerow(dictionary)

    @classmethod
    def load_from_file_csv(cls):
        """
        Deserializes in csv
        """
        filename = cls.__name__ + ".csv"
        if os.path.exists(filename):
            list_dict = []
            with open(filename, 'r', encoding='utf-8') as f:
                csv_reader = csv.DictReader(f)
                for row in csv_reader:
                    dictionary = {key: int(v) for key, v in row.items()}
                    list_dict.append(dictionary)
                return [cls.create(**obj) for obj in list_dict]
        else:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """
        draws Rectangles and squares using turtle module
        """
        drawing = turtle.Turtle()
        drawing.screen.bgcolor("#EDF7F6")
        drawing.shape("turtle")
        drawing.pensize(5)
        drawing.color("#56351E")

        for r in list_rectangles:
            drawing.showturtle()
            drawing.begin_fill()
            drawing.fillcolor("#c47335")
            drawing.up()
            drawing.goto(r.x, r.y)
            drawing.down()
            for i in range(2):
                drawing.forward(r.width)
                drawing.left(90)
                drawing.forward(r.height)
                drawing.left(90)
            drawing.end_fill()
            drawing.hideturtle()

        for s in list_squares:
            drawing.showturtle()
            drawing.begin_fill()
            drawing.fillcolor("#F19953")
            drawing.up()
            drawing.goto(s.x, s.y)
            drawing.down()
            for i in range(4):
                drawing.forward(s.size)
                drawing.left(90)
            drawing.hideturtle()
        drawing.end_fill()
