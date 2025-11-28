#!/usr/bin/python3
"""
Checks if an object is an instance of a class that
inherited from the specified class or not
"""


def inherits_from(obj, a_class):
    """returns true or false"""
    return isinstance(obj, a_class) and type(obj) is not a_class
