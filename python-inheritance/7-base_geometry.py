#!/usr/bin/python3
"""This module contains a class BaseGeometry"""


class BaseGeometry:
    """
    A class to be determined

    Attributes: None
    """

    def __init__(self):
        """Init method"""

        pass

    def area(self):
        """Empty function"""

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        elif value <= 0:
            raise ValueError(f"{name} must be greater than 0")
