#!/usr/bin/python3
"""This function adds all unique integers in a list."""


def uniq_add(my_list=[]):
    uniques = set(my_list)
    return sum(uniques)
