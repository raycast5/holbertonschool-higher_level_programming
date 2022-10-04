#!/usr/bin/python3
"""This module contains a function for testing"""


def write_file(filename="", text=""):
    """Writes text to a given file

    Args:
    filename: name of file to add text to
    text: text to add to file

    Returns:
    Number of characters written

    """

    with open(filename, "w+", encoding="utf-8") as file1:
        return file1.write(str(text))
