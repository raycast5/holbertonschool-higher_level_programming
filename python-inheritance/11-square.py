#!/usr/bin/python3
"""This module contains a class BaseGeometry"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    A subclass of Rectangle

    Attributes: None
    """
    def __init__(self, size):
        super().integer_validator("size", size)

        self.__height = size
        self.__width = size

    def __str__(self):
        return (f"[Square] {self.__width}/{self.__height}")

    def area(self):
        return self.__height * self.__width
