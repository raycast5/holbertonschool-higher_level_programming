#!/usr/bin/python3
def add_integer(a, b=98):
    """Adds two given integers or floats

    Args:
    a: An integer or float
    b: An integer or float

    Returns:
    The result of a plus b

    Raises:
    TypeError: If any given parameter is not an integer or float

    """

    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    else:
        return int(a) + int(b)
