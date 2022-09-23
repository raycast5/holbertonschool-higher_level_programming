#!/usr/bin/python3
""""Create a class"""


class Square:
    """"A new class called square

    Args:
        size (int): Integer representing size of square

    """

    def __init__(self, size=0):

        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if isinstance(value, int) is False:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        return int(self.__size) * int(self.__size)
