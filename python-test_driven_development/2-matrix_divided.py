#!/usr/bin/python3
"""This module contins an addition function for testing"""


def matrix_divided(matrix, div):
    """ Divides every element of a matrix:

    Args:
    matrix: A list of lists
    div: Number to divide the matrix by

    Returns:
    A new list with the result of all divisions

    Raises:
    TypeError: If matrix parameter is not a matrix or it's items
    are  not integers or floats. Also if every row of the matrix
    is not the same size or if div is not an integer or float.

    ZeroDivisionError: If div is equal to 0 or any of the matrix
    elements is 0

    """

    new_matrix = []
    if type(matrix) is list:
        for row in matrix:
            if type(row) is list:
                row_length = len(matrix[0])
            else:
                raise TypeError("matrix must be a matrix \
                                (list of lists) of integers/floats")
            if len(row) != row_length:
                raise TypeError("Each row of the matrix \
                                must have the same size")
            else:
                new_matrix_row = []
            for number in row:
                if type(number) not in [int, float]:
                    raise TypeError("matrix must be a matrix \
                                    (list of lists) of integers/floats")
                elif number == 0 or div == 0:
                    raise ZeroDivisionError("division by zero")
                else:
                    new_matrix_row.append(round((number / div), 2))
            new_matrix.append(new_matrix_row)
        return new_matrix
    else:
        raise TypeError("matrix must be a matrix \
                        (list of lists) of integers/floats")
