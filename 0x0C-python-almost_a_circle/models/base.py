#!/usr/bin/python3
"""
    A module containing the class 'Base'\
    This class will be the “base” of all\
    other classes in this project.\
    The goal of it is to manage id attribute\
    in all your future classes and to avoid\
    duplicating the same code (by extension, same bugs).
"""
import json


class Base:
    """
        A base class with private class attribute '__nb_objects'
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
            Initialize the attributes.
            arg:
                id - argument value of id
                'self.id' - public instance attribute id
        """
        if id is not None and type(id) is not int:
            raise TypeError("id must be an integer")
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
            Returns the JSON string representation of list_dictionaries
            list_dictionaries is a list of dictionaries.
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
            writes the JSON string representation of list_objs to a file(Rectangle.json):
            list_objs is a list of instances(objects) who inherits of Base\
            example: list of Rectangle or list of Square instances
            If list_objs is None, save an empty list
        """
        if list_objs is None or list_objs == []:
            lis_t = "[]"
        else:
            lis_t = cls.to_json_string([i.to_dictionary() for i in list_objs])
        Rectangle = cls.__name__ + ".json"
        with open(Rectangle, 'w') as f:
            f.write(lis_t)

    @staticmethod
    def from_json_string(json_string):
        """
            Returns the list of the JSON string representation of 'json_string'
            json_string is a string representing a list of dictionaries
        """
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)

