#!/usr/bin/python3
"""This function returns a key with the biggest integer value."""


def best_score(a_dictionary):
    if a_dictionary is not None:
        return max(a_dictionary, key=a_dictionary.get)
    return None
