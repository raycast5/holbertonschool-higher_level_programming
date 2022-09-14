#!/usr/bin/python3
"""This function prints returns the first two tuples"""


def add_tuple(tuple_a=(), tuple_b=()):
    l1 = len(tuple_a)
    l2 = len(tuple_b)

    a = 0 if l1 < 1 else tuple_a[0]
    b = 0 if l2 < 1 else tuple_b[0]
    c = 0 if l1 < 2 else tuple_a[1]
    d = 0 if l2 < 2 else tuple_b[1]
    tuple_c = (a + b, c + d)
    return tuple_c
