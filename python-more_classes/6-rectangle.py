#!/usr/bin/python3
"""This module defines a Rectangle class."""


class Rectangle:
    """this class represents a rectangle"""
    number_of_instances = 0
    def __init__(self, width=0, height=0):
        """initializes the width and height"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if isinstance(value, int):
            if value < 0:
                raise ValueError("height must be >= 0")
            else:
                self.__height = value
        else:
            raise TypeError("height must be an integer")

    def perimeter(self):
        if self.__height == 0 or self.__width == 0:
            return 0
        return (self.__width + self.__height)*2

    def area(self):
        return self.__width * self.__height

    def __str__(self):
        if self.width == 0 or self.height == 0:
            return ""
        res = ""
        for i in range(self.__height):
            for j in range(self.__width):
                res += "#"
            res += ("\n" if not i == self.__height - 1 else "")
        return res

    def __repr__(self):
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
