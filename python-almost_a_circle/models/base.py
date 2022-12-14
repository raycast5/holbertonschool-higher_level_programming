#!/usr/bin/python3
""""Module containing a class"""

import json


class Base:
    """"A new class called Base

    Args:
    id (int): id attribute of future classes.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Converts a list of dis to Json string

        Args:
        list_dictionaries: A list of dictionaries

        Returns:
        A JSON string representation of the list

        """

        if list_dictionaries is None:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Saves a list of objects to a file

        Args:
        cls: The class
        list_obj: A list of objects

        Returns:
        Nothing

        """
        list1 = []
        name = cls.__name__ + ".json"
        if list_objs is not None:
            for obj in list_objs:
                list1.append(cls.to_dictionary(obj))

        with open(name, "w+", encoding="utf-8") as f:
            f.write(cls.to_json_string(list1))

    @staticmethod
    def from_json_string(json_string):
        """
        Returns the list of string representation

        Args:
        json_string: A string representing a list of dictionaries

        Returns:
        List of  JSON string representation
        """

        if json_string is None:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        Creates a new instance

        Args:
        cls: class of the instance to be created
        dictionary: dictionary with the parameters of the new instance.

        Returns:
        Instance with all attributes already set:
        """
        if cls.__name__ == "Rectangle":
            new_inst = cls(width=2, height=2)
        elif cls.__name__ == "Square":
            new_inst = cls(size=2)
        new_inst.update(**dictionary)
        return new_inst

    @classmethod
    def load_from_file(cls):
        """Returns a list instances"""
        new_list = []
        in_list = []
        filename = f"{cls.__name__}" + ".json"
        try:
            with open(filename, "r", encoding="utf-8") as f:
                new_list = cls.from_json_string(f.read())
                [in_list.append(cls.create(**inst)) for inst in new_list]
        except Exception:
            pass
        finally:
            return in_list
