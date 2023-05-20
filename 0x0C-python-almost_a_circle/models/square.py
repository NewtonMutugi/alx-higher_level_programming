#!/usr/bin/python3
"""Square class inherits from Rectangle"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """Sqaure class that inherits from Rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize Square class"""
        super().__init__(size, size, x, y, id)
        self.size = size
        self.__x = x
        self.__y = y
        self.__id = id

    def __str__(self):
        """Return string representation of Square"""
        return "[{}] ({}) {}/{} - {}".format(self.__name, self.id,
                                             self.__x, self.__y,
                                             self.__width)

    @property
    def size(self):
        """Getter for size"""
        return self.__width

    @size.setter
    def size(self, value):
        """Setter for size"""
        self.__width = value
        self.__height = value
