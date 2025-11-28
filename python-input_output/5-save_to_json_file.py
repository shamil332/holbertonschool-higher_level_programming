#!/usr/bin/python3
"""module for the task 5"""
import json


def save_to_json_file(my_obj, filename):
    """writes obj to a file"""
    with open(filename, "w", encoding="utf-8") as f:
        f.dump(my_obj, f)
