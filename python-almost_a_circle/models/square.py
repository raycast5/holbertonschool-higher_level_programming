#!/usr/bin/python3
"""This module contains a class BaseGeometry"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """A subclass of Rectangle that makes a new square"""

    def __init__(self, size, x=0, y=0, id=None):
        """Constructor for the class Square"""

        self.size = size
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Returns a str representation of rectangle"""

        return (f"[Square] ({self.id}) {self.__x}/{self.__y} - " +
                f"{self.size}")
