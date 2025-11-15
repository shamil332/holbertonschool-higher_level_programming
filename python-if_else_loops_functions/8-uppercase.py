#!/usr/bin/python3
def uppercase(str):
    nw_s = ""
    for c in str:
        if 'a' <= c <= 'z':
            nw_s += chr(ord(c) - 32)
        else:
            nw_s += c
    print("{}".format(nw_s))
