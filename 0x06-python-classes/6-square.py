#!/usr/bin/python3
"""This module defines a class Square"""


class Square:
    """This class defines a square"""

    def __init__(self, size=0, position=(0, 0)):
        """Initializes the square
        Args:
        size (int): private size of the square
                position (tuple): private position of the square"""

        if type(size) is not int:
            raise TypeError("size must 	be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
            if type(position) is not tuple:
                raise TypeError("position must be a tuple")
            elif len(position) != 2:
                raise ValueError("position must be a 2-tuple")
            elif type(position[0]) is not int or type(position[1]) is not int:
                raise TypeError("position must be a 2-tuple of integers")
            elif position[0] < 0 or position[1] < 0:
                raise TypeError("position must be a 2-tuple of positive int")
            else:
                self.__position = position

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

    @property
    def position(self):
        """Returns: the position of the square"""

        return self.__position

    @position.setter
    def position(self, value):
        """Sets the position of the square
        Args:
        value (tuple): the new position of the square"""
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def my_print(self):
        """Prints the square"""

        if self.__size == 0:
            print()
            return
        else:
            for i in range(self.__position[1]):
                print()
            for i in range(self.__size):
                for j in range(self.__position[0]):
                    print(" ", end="")
                for j in range(self.__size):
                    print("#", end="")
                print()
