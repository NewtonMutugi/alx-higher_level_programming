#!/usr/bin/python3
"""This module defines a class Square"""


class Square:
    """This class defines a square"""

    def __init__(self, size=0):
        """Initializes the square
        Args:
        size (int): private size of the square"""

        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """Returns: the area of the square"""

        return self.__size ** 2

    @property
    def size(self):
        """Returns: the size of the square"""

        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size of the square
        Args:
        value (int): the new size of the square"""

        if type(value) is not int:
            raise TypeError("value must be an integer")
        elif value < 0:
            raise ValueError("value must be >= 0")
        else:
            self.__size = value
