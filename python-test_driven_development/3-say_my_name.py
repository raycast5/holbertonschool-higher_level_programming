#!/usr/bin/python3
"""This module contins a function for testing"""


def say_my_name(first_name, last_name=""):
    """ Prints a name:

    Args:
    first_name: First name
    last_name: Last name

    Returns:
    Nothing

    Raises:
    TypeError: If any of the parameters is not a string.

    """

    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    elif type(last_name) is not str:
        raise TypeError("last_name must be a string")
    else:
        print(f"My name is {first_name} {last_name}")
