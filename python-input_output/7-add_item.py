#!/usr/bin/python3
"""This module adds all args to list and saves to json file"""


from sys import argv
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

try:
    list1 = load_from_json_file("add_item.json")
except:
    list1 = []
finally:
    for args in argv[1:]:
        list1.append(args)
    save_to_json_file(list1, "add_item.json")
