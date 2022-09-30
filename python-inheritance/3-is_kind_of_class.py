#!/usr/bin/python3
"""This module contains a function for testing"""


def is_kind_of_class(obj, a_class):
    """
    Checks if the object is an instance of, or if the object
    is an instance of a class that inherited from,
    the specified class.

    Args:
    obj: an object
    a_class: class to check against

    Returns:
    True if the object is an instance of, or if the object
    is an instance of a class that inherited from,
    the specified class; otherwise False.

    """

    return isinstance(obj, a_class)
