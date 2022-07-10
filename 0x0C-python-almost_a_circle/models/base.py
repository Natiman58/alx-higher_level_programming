#!/usr/bin/python3
"""
    A module containing the class 'Base'\
    This class will be the “base” of all\
    other classes in this project.\
    The goal of it is to manage id attribute\
    in all your future classes and to avoid\
    duplicating the same code (by extension, same bugs).
"""
import os
import csv
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
            Returns a structured data; the list of the JSON string representation of 'json_string'
            json_string is a jason string representing a list of dictionaries.
        """
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """A class method that returns an instance with all attributes set"""
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """
            Returns the list of instances(objects) in the file name(file_name)
            if file name doesn't exist: return empty list
        """
        file_name = cls.__name__ + ".json"
        lis_t = []
        if os.path.exists(file_name):
            with open(file_name, 'r', encoding="utf-8") as f:
                s = f.read()
                l_dict = cls.from_json_string(s)
                for d in l_dict:
                    lis_t.append(cls.create(**d))
        return lis_t

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
            To serialize(to string_ize) list_objs file into a CSV file(file_name.csv)
        """
        if type(list_objs) != list and list_objs is not None or\
                not all(isinstance(i, cls) for i in list_objs):
            raise TypeError("list_objs must be a list of instances.")

        file_name = cls.__name__ + ".csv"
        with open(file_name, 'w', encoding='utf-8', newline='') as csv_file:
            if list_objs is not None:
                list_objs = [i.to_dictionary() for i in list_objs]
                if cls.__name__ == 'Rectangle':
                    field_names = ['id', 'width', 'height', 'x', 'y']
                elif cls.__name__ == 'Square':
                    field_names = ['id', 'size', 'x', 'y']
                writer = csv.DictWriter(csv_file, fieldnames=field_names)
                writer.writeheader()
                writer.writerows(list_objs)

    @classmethod
    def load_from_file_csv(cls):
        """
            To deserialize(reconstruct an object) from a csv file
        """
        file_name = cls.__name__ + '.csv'
        lis_t = []
        if os.path.exists(file_name):
            with open(file_name, 'r') as csv_file:
                reader = csv.reader(csv_file, delimiter=',')
                if cls.__name__ == 'Rectangle':
                    field_names = ['id', 'width', 'height', 'x', 'y']

                elif cls.__name__ == 'Square':
                    field_names = ['id', 'size', 'x', 'y']

                for idx, row in enumerate(reader):
                    if idx > 0:
                        i = cls(1, 1)
                        for j, e in enumerate(row):
                            if e:
                                setattr(i, field_names[j], int(e))
                        lis_t.append(i)

        return lis_t
