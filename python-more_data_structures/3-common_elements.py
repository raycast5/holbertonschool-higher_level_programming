#!/usr/bin/python3
"""This function returns a set of common elements in two sets."""


def common_elements(set_1, set_2):
    set_3 = {x for x in set_1 if x in set_2}
    return set_3
