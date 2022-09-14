#!/usr/bin/python3
"""This function finds the biggest integer in a list"""


def max_integer(my_list=[]):
    if my_list is not None:
        for i in range(my_list[-1]):
            if my_list[i] > my_list[i + 1]:
                temp = my_list[i]
        return temp
    else:
        return None
