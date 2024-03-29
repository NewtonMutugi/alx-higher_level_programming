#!/usr/bin/python3
"""Module to add attributes to an object"""


def add_attribute(obj, name, value):
    """Function to add attributes to an object"""
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, name, value)
    return obj
