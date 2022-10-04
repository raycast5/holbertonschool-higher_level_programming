#!/usr/bin/python3
"""This module contains a function for testing"""


import json


def load_from_json_file(filename):
    """Creates an Object from a “JSON file”:

    Args:
    filename: name of file to read from

    Returns:
    Nothing

    """

    with open(filename, "r", encoding="utf-8") as file1:
        return json.load(file1)
