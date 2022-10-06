#!/usr/bin/python3
"""This module contains a class BaseGeometry"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """A subclass of Rectangle that makes a new square"""

    def __init__(self, size, x=0, y=0, id=None):
        """Constructor for the class Square"""

        self.size = size
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Retrieves Square size"""
        return self.width

    @size.setter
    def size(self, value):
        """Sets Square size."""
        self.width = value
        self.height = value

    def __str__(self):
        """Returns a str representation of square"""

        return (f"[Square] ({self.id}) {self.x}/{self.y} - " +
                f"{self.size}")

    def update(self, *args, **kwargs):
        """Updates the instance attributes"""
        arg_list = ["id", "size", "x", "y"]
        if args:
            for a in range(len(args)):
                setattr(self, arg_list[a], a)
        else:
            for k, v in kwargs.items():
                setattr(self, k, v)
