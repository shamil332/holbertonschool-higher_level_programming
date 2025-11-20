#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    return {k: (lambda x: x*2)(v) for k, v in a_dictionary.items()}
