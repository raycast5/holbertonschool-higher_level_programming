#!/usr/bin/python3
for x in range(9):
    for y in range(x, 10):
        if x != y:
            print("{:d}{:d}".format(x, y),
                   end=", " if x != 8 else "\n")
