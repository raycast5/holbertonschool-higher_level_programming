#!/usr/bin/python3
"""This module contains a function for testing"""


import json


def from_json_string(my_str):
    """returns an object represented by a JSON string:

    Args:
    my_str: string to be deserialized

    Returns:
    an object represented by a JSON strin

    """

    return json.loads(my_str)
