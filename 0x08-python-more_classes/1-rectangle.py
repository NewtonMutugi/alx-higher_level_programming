class Rectangle:
    """Rectangle class with width and height attributes"""

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle with `width` and `height`.
        Args:
            width (int): The width of the new Rectangle.
            height (int): The height of the new Rectangle.
        """

        self.width = width
        self.height = height

    @property
    def width(self):
        """int: The width of the Rectangle."""
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
        """int: The height of the Rectangle."""
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
