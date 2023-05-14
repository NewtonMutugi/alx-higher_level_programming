#!/usr/bin/python3
"""Module that defines a class Student"""


class Student:
    """Defines a student"""

    def __init__(self, first_name, last_name, age):
        """Initializes a student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, atrributes=None):
        """retrieves a dictionary representation of a Student instance
        If attrs is a list of strings, only attribute names contained
        in this list must be retrieved."""
        if type(atrributes) is not list:
            return self.__dict__
        else:
            new_dict = {}
            for key, value in self.__dict__.items():
                if key in atrributes:
                    new_dict[key] = value
            return new_dict
