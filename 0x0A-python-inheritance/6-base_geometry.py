#!/usr/bin/python3
"""Module that defines a class BaseGeometry"""


class BaseGeometry:
    """Class that defines a BaseGeometry"""

    def area(self):
        """Function that raises an Exception with the message
        'area() is not implemented'"""
        raise Exception("area() is not implemented")
