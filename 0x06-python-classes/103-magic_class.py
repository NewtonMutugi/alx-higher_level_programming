#!/usr/bin/python3
"""Define a MagicClass"""

import math


class MagicClass:
    """class that represents the MagicClass"""

    def __init__(self, radius=0):
        """Initialize the MagicClass.
        Args:
        radius (int): The radius of the MagicClass.
        Raises:
        TypeError: If radius is not an integer or float."""
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """Return the area of the MagicClass."""
        return (self.__radius ** 2 * math.pi)

    def circumference(self):
        """Return The circumference of the MagicClass."""
        return (2 * math.pi * self.__radius)
