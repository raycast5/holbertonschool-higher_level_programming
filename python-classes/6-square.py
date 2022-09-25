#!/usr/bin/python3
""""Create a class"""


class Square:
    """"A new class called square

    Args:
        size (int): Integer representing size of square

    """

    def __init__(self, size=0, position=(0, 0)):

        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        return self.__position

    @position.setter
    def postion(self, coord):
        if isinstance(coord, tuple) is True and \
          isinstance(coord[0], int) is True and \
          isinstance(coord[1], int) is True and \
          coord[0] >= 0 and \
          coord[1] >= 0:
            self.__position = coord
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

    def area(self):
        return int(self.__size) * int(self.__size)

    def my_print(self):
        size = self.size
        position = self.position
        if size == 0:
            print("")
        else:
            for row in range(size):
                for space in range(position[0]):
                    print(" ", end="")
                for item in range(size):
                    print("#", end="")
                print("")
