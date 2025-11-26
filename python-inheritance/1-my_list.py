#!/usr/bin/python3
"""
This module defines a class MyList that inherits from the built-in list class.
It includes a public method to print the list in ascending sorted order.
"""


class MyList(list):
    """
    MyList class inherits from the built-in list and adds a method
    to print the list sorted in ascending order.
    """

    def print_sorted(self):
        """
        Prints the list in ascending sorted order without modifying
        the original list.
        """
        print(sorted(self))
