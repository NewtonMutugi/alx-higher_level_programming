#!/usr/bin/python3
"""Square class inherits from Rectangle"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """Sqaure class that inherits from Rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize Square class"""
        self.size = size
        self.__x = x
        self.__y = y
        self.__id = id
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Getter for size"""
        return self.__width

    @size.setter
    def size(self, value):
        """Setter for size"""
        self.__width = value
        self.__height = value

    def __str__(self):
        """Returns string representation of Square"""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                 self.width)
