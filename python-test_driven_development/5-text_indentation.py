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
        raise TypeError("text must be a string")
    else:
        for sep in ":.?":
            text = (sep+"\n\n").join([row.strip() for row in text.split(sep)])
        print(text, end="")
