#!/usr/bin/python3
"""This function prints a dictionary by ordered keys."""


def print_sorted_dictionary(a_dictionary):
    dict2 = dict(sorted(a_dictionary.items()))
    for k, v in dict2.items():
        print(f"{k}: {v}")
