#!/usr/bin/python3
"""This module contains a function for testing"""


import json


def to_json_string(my_obj):
    """Returns the JSON representation of an object (string)

    Args:
    my_obj: string to be serialized

    Returns:
    JSON representation of an object (string)

    """

    return json.dumps(my_obj)
