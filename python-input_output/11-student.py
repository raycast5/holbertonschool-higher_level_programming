#!/usr/bin/python3
""""Module that contains a class named Student"""


class Student:
    """"
    A new class called Student

    Args:
    first_name (str): First name of student
    last_name (str): Last name of student
    age (int): Age of student

    """

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        json_dic = self.__dict__
        if type(attrs) is list:
            if all(isinstance(s, str) for s in attrs):
                return {k: v for k, v in json_dic.items() if k in attrs}
        else:
            return json_dic
    
    def reload_from_json(self, json):
        for k, v in json.items():
            if k in self.__dict__:
                self.k = v
