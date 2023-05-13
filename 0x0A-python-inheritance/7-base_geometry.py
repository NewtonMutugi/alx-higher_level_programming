#!/usr/bin/python3
"""Module that defines a class BaseGeometry"""


class BaseGeometry:
    """Class that defines a BaseGeometry"""

    def area(self):
        """Function that raises an Exception with the message
        'area() is not implemented'"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Function that validates value"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
