#!/usr/bin/python3
"""This function removes the letter c from any string"""


def no_c(my_string):

    temp = my_string.translate({ord("c"): None})
    temp2 = temp.translate({ord("C"): None})
    return temp2
