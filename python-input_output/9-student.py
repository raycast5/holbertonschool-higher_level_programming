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

    def to_json(self):
        return self.__dict__
