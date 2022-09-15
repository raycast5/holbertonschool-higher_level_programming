#!/usr/bin/python3
"""This function replaces all occurrences of
    an element by another in a new list."""


def search_replace(my_list, search, replace):
    new_list = [i if i != search else replace for i in my_list]
    return new_list
