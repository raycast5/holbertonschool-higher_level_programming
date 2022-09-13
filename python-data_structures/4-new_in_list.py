#!/usr/bin/python3
"""This function rep laces an element of a list in a copy"""


def new_in_list(my_list, idx, element):
    dganger = my_list.copy()
    if idx < 0 or idx >= len(my_list):
        return dganger
    else:
        dganger[idx] = element
        return dganger
