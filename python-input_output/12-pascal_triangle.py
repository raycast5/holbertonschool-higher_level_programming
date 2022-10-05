#!/usr/bin/python3
"""This module contains a function for testing"""


def pascal_triangle(n):
    """
    Function to calculate the pascal triangle of n:

    Args:
    n: an integer

    Returns:
    A list of lists of integers representing the
    pascal triangle of n

    """

    triangle = []
    if n > 0:
        for row in range(n):
            triangle.append([])
            triangle[row].append(1)
            for number in range(1, row):
                triangle[row].append(triangle[row - 1][number - 1] +
                                     triangle[row - 1][number])
            if row != 0:
                triangle[row].append(1)
    return triangle
