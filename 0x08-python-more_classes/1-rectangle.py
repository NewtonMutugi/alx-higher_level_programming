#!/usr/bin/python3
""" Contains class Rectangle that defines a rectangle"""


class Rectangle:
    """Rectangle Definition"""
    __width = 0

    def width(self):
        """getter for __width attribute"""
        return self.__width

    def width(self, value):
        """setter for __width attribute"""
        self.__width = value

    __height = 0

    def height(self):
        """getter for __height attribute"""
        return self.__height

    def height(self, value):
        """setter for __height attribute"""
        self.__height = value

    def __init__(self, width=0, height=0):
        """Initializes rectangle size"""
        self.__width = width
        self.__height = height
