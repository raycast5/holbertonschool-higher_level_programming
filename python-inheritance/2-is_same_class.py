#!/usr/bin/python3
"""This module contains a function for testing"""


def is_same_class(obj, a_class):
    """
    Checks if the object is exactly an
    instance of the specified class.

    Args:
    obj: an object
    a_class: class to check against

    Returns:
    True if the object is exactly an instance of
    the specified class ; otherwise False.

    """

    return type(obj) is a_class
