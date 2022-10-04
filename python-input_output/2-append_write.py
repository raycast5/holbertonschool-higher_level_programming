#!/usr/bin/python3
"""This module contains a function for testing"""


def append_write(filename="", text=""):
    """Appends text to a given file

    Args:
    filename: name of file to add text to
    text: text to add to file

    Returns:
    Number of characters written

    """

    with open(filename, "a+", encoding="utf-8") as file1:
        return file1.write(str(text))
