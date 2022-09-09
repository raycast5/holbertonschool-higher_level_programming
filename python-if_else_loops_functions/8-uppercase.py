#!/usr/bin/python3
def uppercase(str):
    for a in str:
        if ord(a) in range(96, 123):
            a = chr(ord(a) - 32)
        print("{:s}".format(a), end="")
    print("")
