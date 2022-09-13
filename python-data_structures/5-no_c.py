#!/usr/bin/python3
"""This function removes the letter c from any string"""


def no_c(my_string):

    temp = my_string.translate({ord(i): None for i in "cC"})
    return temp
