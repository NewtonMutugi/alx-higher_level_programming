#!/usr/bin/python3
"""This module defines a class Square"""


class Square:
    """This class defines a square"""

    def __init__(self, size=0):
        """Initializes the square
        Args:
        size (int): private size of the square"""
        self.size = size

    def area(self):
        """Returns: the area of the square"""

        return (self.__size) ** 2

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
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def __eq__(self, sq):
        """Returns: True if the square is equal to the value"""
        return self.area() == sq.area()

    def __ne__(self, sq):
        """Returns: True if the square is not equal to the value"""
        return self.area() != sq.area()

    def __lt__(self, sq):
        """Returns: True if the square is less than the value"""
        return self.area() < sq.area()

    def __gt__(self, sq):
        """Returns: True if the square is greater than the value"""
        return self.area() > sq.area()

    def __le__(self, sq):
        """Returns: True if the square is less than or equal to the value"""
        return self.area() <= sq.area()

    def __ge__(self, sq):
        """Returns: True if the square is greater than or equal to the value"""
        return self.area() >= sq.area()
