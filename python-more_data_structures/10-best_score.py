#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        best = sorted(a_dictionary, reverse=True)[0]
        return best
    else:
        return None
