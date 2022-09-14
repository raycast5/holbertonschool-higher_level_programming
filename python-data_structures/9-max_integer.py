#!/usr/bin/python3
"""This function finds the biggest integer in a list"""


def max_integer(my_list=[]):
    len1 = len(my_list)
    if len1 == 0:
        return None
    else:
        max = my_list[0]
        for i in my_list:
            if max < i:
                max = i
        return max
