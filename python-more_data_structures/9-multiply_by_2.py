#!/usr/bin/python3
"""This function returns a new dictionary
    with all values multiplied by 2."""


def multiply_by_2(a_dictionary):
    dict2 = {k: v * 2 for k, v in a_dictionary.items()}
    return dict2
