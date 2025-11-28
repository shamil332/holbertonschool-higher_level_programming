#!/usr/bin/python3
"""module for task 1"""


def read_file(filename=""):
    """Reads a UTF-8 text file and prints it to stdout."""
    with open(filename, 'r', encoding="utf-8") as f:
        print(f.read(), end="")
