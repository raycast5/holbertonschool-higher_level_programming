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
        return self.__size

    @size.setter
    def size(self, value):
        """Sets Square size."""

        if isinstance(value, int) is False:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.width = value
            self.height = value

    def __str__(self):
        """Returns a str representation of square"""

        return (f"[Square] ({self.id}) {self.x}/{self.y} - " +
                f"{self.size}")
