#!/usr/bin/python3
"""This module contains a class MyList that inherits from list"""


class MyList(list):
    """
    A class that inherits from list

    Attributes: None
    """

    def print_sorted(self):
        """Prints a sorted list of ints"""

        print(sorted(self))
