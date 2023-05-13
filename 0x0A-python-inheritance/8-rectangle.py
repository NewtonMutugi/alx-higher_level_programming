#!/usr/bin/python3
"""Module 8-rectangle"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry
bg = BaseGeometry()


class Rectangle:
    """Rectangle class"""

    def __init__(self, width, height):
        """Initialization method"""

        bg.integer_validator("width", width)
        bg.integer_validator("height", height)

        self.__width = width
        self.__height = height
