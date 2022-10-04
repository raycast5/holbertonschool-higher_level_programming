#!/usr/bin/python3
"""This module contains a function for testing"""


def class_to_json(obj):
    """ 
    Returns the dictionary description of a
    class with simple data structures for JSON
    serializing.

    Args:
    obj: A python class

    Returns:
    A dictionary representaion of a class

    """

    return obj.__dict__
