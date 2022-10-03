#!/usr/bin/python3
""""Create a class"""


class Rectangle:
    """"A new class called Rectangle

    Args:
        width (int): Integer representing width of square
        height (int):  Integer representing height of square

    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        self.print_symbol = Rectangle.print_symbol
        Rectangle.number_of_instances += 1

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
                    rectangle.append(str(self.print_symbol))
                if y != self.__height - 1:
                    rectangle.append("\n")
            return "".join(rectangle)

    def __repr__(self):
        return (f"Rectangle({self.__width}, {self.__height})")

    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if isinstance(rect_1, Rectangle) is False:
            raise TypeError("rect_1 must be an instance of Rectangle")
        elif isinstance(rect_2, Rectangle) is False:
            raise TypeError("rect_2 must be an instance of Rectangle")
        else:
            if rect_2.area() > rect_1.area():
                return rect_2
            else:
                return rect_1

    @classmethod
    def square(cls, size=0):
        return cls(size, size)
