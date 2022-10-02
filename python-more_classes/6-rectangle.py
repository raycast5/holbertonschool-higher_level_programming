#!/usr/bin/python3
""""Create a class"""


class Rectangle:
    """"A new class called Rectangle

    Args:
        width (int): Integer representing width of square
        height (int):  Integer representing height of square

    """


    number_of_instances = 0

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        number_of_instances += 1

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if isinstance(value, int) is False:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if isinstance(value, int) is False:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return 2 * (self.__width + self.__height)

    def __str__(self):
        rectangle = []
        if self.__width == 0 or self.__height == 0:
            return ""
        else:
            for y in range(self.__height):
                for x in range(self.__width):
                    rectangle.append("#")
                if y != self.__height - 1:
                    rectangle.append("\n")
            return "".join(rectangle)

    def __repr__(self):
        return (f"Rectangle({self.__width}, {self.__height})")

    def __del__(self):
        print("Bye rectangle...")
        number_of_instances -= 1
