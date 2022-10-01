#!/usr/bin/python3
"""This module contains a class BaseGeometry"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    A subclass of BaseGeometry

    Attributes: None
    """
    def __init__(self, width, height):
        super().integer_validator("height", height)
        super().integer_validator("width", width)

        self.__height = height
        self.__width = width
