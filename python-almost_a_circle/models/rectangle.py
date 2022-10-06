#!/usr/bin/python3
"""This module contains a class BaseGeometry"""


from models.base import Base


class Rectangle(Base):
    """A subclass of Base that makes a new rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Constructs a new rectangle

        Args:
            width (int): Integer representing width of rectangle
            height (int):  Integer representing height of rectangle
            x (int): Coords of rectangle
            y (int): Coords of rectangle

        Raises:
            TypeError: If input is not an int
            ValueError: If width or height <= 0 and x or y < 0
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Retrieves rectangle width."""

        return self.__width

    @width.setter
    def width(self, value):
        """Sets rectangle width."""

        if isinstance(value, int) is False:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Retrieves rectangle height."""

        return self.__height

    @height.setter
    def height(self, value):
        """Sets rectangle height."""

        if isinstance(value, int) is False:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    @property
    def x(self):
        """Retrieves x coord of rectangle."""

        return self.__x

    @x.setter
    def x(self, value):
        """Sets x coord of rectangle."""

        if isinstance(value, int) is False:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    @property
    def y(self):
        """Retrieves y coord of rectangle."""

        return self.__y

    @y.setter
    def y(self, value):
        """Sets y coord of rectangle."""

        if isinstance(value, int) is False:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value

    def area(self):
        """Returns the area of rectangle"""

        return self.__width * self.__height

    def display(self):
        """Prints a represenation of rectangle
            to std output"""

        for y in range(self.__y):
            print("")
        for row in range(self.__height):
            for x in range(self.__x):
                print(" ", end="")
            for item in range(self.__width):
                print("#", end="" if item != self.__width - 1 else "\n")

    def __str__(self):
        """Returns a str representation of rectangle"""

        return (f"[Rectangle] ({self.id}) {self.__x}/{self.__y} - " +
                f"{self.__width}/{self.__height}")

    def update(self, *args, **kwargs):
        """Updates the instance attributes"""
        arg_list = ["id", "width", "height", "x", "y"]
        if args:
            for a in range(len(args)):
                setattr(self, arg_list[a], args[a])
        else:
            for k, v in kwargs.items():
                setattr(self, k, v)

    def to_dictionary(self):
        """Returns the dictionary representation of Rectangle"""
        return self.__dict__
