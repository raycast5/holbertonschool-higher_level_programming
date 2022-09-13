#!/usr/bin/python3
"""This function prints a matrix of integers"""


def print_matrix_integer(matrix=[[]]):
    if matrix is not None:
        for a in matrix:
            for b in a:
                print("{:d}".format(b), end=" ")
            print()
