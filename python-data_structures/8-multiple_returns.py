#!/usr/bin/python3
"""This function returns a tuple with the length
    of a string and its first character"""


def multiple_returns(sentence):
    a = len(sentence)
    b = sentence[0] if a > 0 else None
    return a, b
