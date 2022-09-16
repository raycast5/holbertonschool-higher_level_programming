#!/usr/bin/python3
"""A function that divides 2 integers and prints the result."""


def safe_print_division(a, b):
    result = None
    try:
        result = a / b
    except ZeroDivisionError:
        pass
    finally:
        print(f"Inside result: {result}")
        return result
