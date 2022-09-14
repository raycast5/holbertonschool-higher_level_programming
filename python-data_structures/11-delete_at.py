#!/usr/bin/python3
"""This function deletes an item from list at specified index"""


def delete_at(my_list=[], idx=0):
    if idx in range(len(my_list)):
        del my_list[idx]
    return my_list
