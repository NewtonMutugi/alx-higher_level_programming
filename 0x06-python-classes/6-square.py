#!/usr/bin/python3
"""This module defines a class Square"""


class Square:
    """This class defines a square"""

    def __init__(self, size=0, position=(0, 0)):
        """Initializes the square
        Args:
        size (int): private size of the square
                position (tuple): private position of the square
        """
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """Returns: the size of the square"""

        return (self.__size)

    @size.setter
    def size(self, value):
        """Sets the size of the square
        Args:
        value (int): the new size of the square"""

        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Returns: the position of the square"""

        return (self.__position)

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

    def area(self):
        """Returns: the area of the square"""

        return (self.size * self.size)

    def my_print(self):
        """Prints the square"""

        if self.__size == 0:
            print()
            return

        [print("") for i in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print(" ", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]
            print("")