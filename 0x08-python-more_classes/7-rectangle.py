#!/usr/bin/python3
"""This module defines a class Rectangle."""


class Rectangle:
    """Rectangle class with width and height attributes"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle with `width` and `height`.
        Args:
            width (int): The width of the new Rectangle.
            height (int): The height of the new Rectangle.
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """int: the width of the rectangle."""
        return self._width

    @width.setter
    def width(self, value):
        """The width of the Rectangle.
        Args:
            value (int): The new width of the Rectangle.
        Raises:
            TypeError: If `value` is not an int.
            ValueError: If `value` is negative.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self._width = value

    @property
    def height(self):
        """int: the height of the rectangle."""
        return self._height

    @height.setter
    def height(self, value):
        """The height of the Rectangle.
        Args:
            value (int): The new height of the Rectangle.
        Raises:
            TypeError: If `value` is not an int.
            ValueError: If `value` is negative.
        """

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self._height = value

    def area(self):
        """Return the area of the Rectangle."""
        return self.width * self.height

    def perimeter(self):
        """Return the perimeter of the Rectangle."""
        if self.width == 0 or self.height == 0:
            return 0
        else:
            return 2 * (self.width + self.height)

    def __str__(self):
        """Return the printable representation of the Rectangle.
        Represents the rectangle with the # character.
        """
        if self.width == 0 or self.height == 0:
            return ""
        else:
            return "\n".join([str(self.print_symbol)
                              * self.width] * self.height)

    def __repr__(self):
        """Return the string representation of the Rectangle."""

        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """Delete the Rectangle."""

        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
