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
        self.__id = None
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Getter for size"""
        return self.width

    @size.setter
    def size(self, value):
        """Setter for size"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Update attributes of Square"""
        if args:
            attrs = ["id", "size", "x", "y"]
            for i, arg in enumerate(args):
                setattr(self, attrs[i], arg)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Returns dictionary representation of Square"""
        attrs = ["id", "size", "x", "y"]
        return {key: getattr(self, key) for key in attrs}

    def __str__(self):
        """Returns string representation of Square"""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                 self.width)
