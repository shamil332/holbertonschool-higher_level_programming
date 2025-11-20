#!/usr/bin/python3
def roman_to_int(roman_string):
    roman = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }
    if not isinstance(roman_string, str) or roman_string == None:
        return None
    total = 0
    for i in range(len(roman_string)):
        value = roman[roman_string[i]]
        if i+1 == len(roman_string) or value >= roman[roman_string[i+1]]:
            total += value
        else:
            total -= value
    return total
