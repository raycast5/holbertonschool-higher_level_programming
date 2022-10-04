#!/usr/bin/python3
"""This module contains a function for testing"""


def read_file(filename=""):
    """Reads a given file and prints it to std output

    Args:
    filename: name of file to be read

    Returns:
    Nothing

    """

    with open(filename, encoding="utf-8") as file1:
        for line in file1.read():
            print(line, end="")
