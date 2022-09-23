#!/usr/bin/python3
""""Create a class"""


class Square:
    """"A new class called square

    Args:
        size (int): Integer representing size of square

    """

    def __init__(self, size=0):
        if isinstance(size, int) is False:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
