#!/usr/bin/python3
"""This function rep laces an element of a list in a c like fashion"""


def replace_in_list(my_list, idx, element):
    if idx < 0 or idx >= len(my_list):
        return my_list
    else:
        my_list[idx] = element
        return my_list
