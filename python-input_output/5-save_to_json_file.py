#!/usr/bin/python3
"""This module contains a function for testing"""


import json


def save_to_json_file(my_obj, filename):
    """Saves to file the JSON representation of an object

    Args:
    my_obj: string to be serialized
    filename: name of file to save to

    Returns:
    Nothing

    """

    with open(filename, "w+", encoding="utf-8") as file1:
        json.dump(my_obj, file1)
