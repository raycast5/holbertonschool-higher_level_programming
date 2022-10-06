#!/usr/bin/python3
"""This module contains a class BaseGeometry"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """A subclass of Rectangle that makes a new square"""

    def __init__(self, size, x=0, y=0, id=None):
        """Constructor for the class Square"""
        self.width = size
        self.height = size
        super().__init__(id, x, y, size, size)
