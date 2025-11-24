#!/usr/bin/python3
"""This module defines a Rectangle class."""

class Rectangle:
    """this class represents a rectangle"""
    def __init__(self, width=0, heigth=0):
        """initializes the width and heigth"""
        self.width = width
        self.heigth = heigth

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if isinstance(value, int):
            if value < 0:
                raise ValueError("width must be >= 0")
            else:
                self.__width = value
        else:
            raise TypeError("width must be an integer")

    @property
    def heigth(self):
        return self.__heigth

    @heigth.setter
    def heigth(self, value):
        if isinstance(value, int):
            if value < 0:
                raise ValueError("height must be >= 0")
            else:
                self.__heigth = value
        else:
            raise TypeError("height must be an integer")
