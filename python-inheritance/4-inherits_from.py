#!/usr/bin/python3
"""This module contains a function for testing"""


def inherits_from(obj, a_class):
    """
    Checks if object is an instance of a class that
    inherited (directly or indirectly) from
    the specified class

    Args:
    obj: an object
    a_class: class to check against

    Returns:
    True if object is an instance of a class that
    inherited (directly or indirectly) from
    the specified class; otherwise False.

    """

    return issubclass(type(obj), a_class)
