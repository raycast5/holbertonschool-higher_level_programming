#!/usr/bin/python3
"""This module contins a function for testing"""


def text_indentation(text):
    """ Prints text and replaces certain characters with newlines

    Args:
    text: A string

    Returns:
    Nothing

    Raises:
    TypeError: If text is not a string

    """
    if type(text) is not str:
        raise TypeError("test must be a string")
    else:
        str1 = text.replace(".", ".\n\n")
        str2 = str1.replace(":", ":\n\n")
        str3 = str2.replace("?", "?\n\n")
        str4 = str3.replace("\n ", "\n")
        str5 = str4.replace(" \n", "\n")
        print(str5, end="")
