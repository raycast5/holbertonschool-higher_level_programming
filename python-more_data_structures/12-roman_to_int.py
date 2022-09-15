#!/usr/bin/python3
"""This function converts roman numerals to int"""


def roman_to_int(roman_string):
    total = 0
    roman_dict = {"I": 1, "V": 5, "X": 10, "L": 50,
                  "C": 100, "D": 500, "M": 1000}
    if isinstance(roman_string, str):
        for i in range(len(roman_string) - 1, -1, -1):
            integ = roman_dict[roman_string[i]]
            if integ * 3 < total:
                total -= integ
            else:
                total += integ
        return total
    else:
        return 0
