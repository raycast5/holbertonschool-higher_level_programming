#!/usr/bin/python3
""""Create a class"""


class Square:
    """"A new class called square

    Args:
        size (int): Integer representing size of square

    """

    def __init__(self, size=0, position=(0, 0)):

        self.size = size
        self.position = position

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
    def position(self, value):
        if isinstance(value, tuple) is True and \
          len(value) == 2 and \
          isinstance(value[0], int) is True and \
          isinstance(value[1], int) is True and \
          value[0] >= 0 and \
          value[1] >= 0:
            self.__position = value
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

    def area(self):
        return int(self.__size) * int(self.__size)

    def my_print(self):
        size = self.size
        position = self.position
        if size == 0 or position[0] == 0:
            print("")
        else:
            for row in range(size):
                for space in range(position[0]):
                    print(" ", end="")
                for item in range(size):
                    print("#", end="")
                print("")
