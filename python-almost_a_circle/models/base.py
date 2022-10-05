#!/usr/bin/python3
""""Module containing a class"""


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
