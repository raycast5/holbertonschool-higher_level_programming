#!/usr/bin/python3
"""This module contins a function for testing"""


def print_square(size):
    """ Prints a square

    Args:
    size: Size of square to be printed

    Returns:
    Nothing

    Raises:
    TypeError: If size is not a string or if size is a
    float and less than 0

    ValueError: If size is less than 0

    """

    if type(size) is not int:
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    else:
        for y in range(size):
            for x in range(size):
                print("#", end="" if x < (size - 1) else "\n")
