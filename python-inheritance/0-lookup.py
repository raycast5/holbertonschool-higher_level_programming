#!/usr/bin/python3
"""This module contains a lookup function for testing"""


def lookup(obj):
    """Returns the list of available attributes and methods of an object

    Args:
    obj: an object

    Returns:
    List of available attributes and methods of an object

    """

    return dir(obj)
