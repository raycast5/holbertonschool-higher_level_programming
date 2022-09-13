#!/usr/bin/python3
"""This function retrieves an element of a list in a c like fashion"""
def element_at(my_list, idx):
    if idx < 0 or idx >= len(my_list):
        return None
    else:
        return my_list[idx]
