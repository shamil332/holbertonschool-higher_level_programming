#!/usr/bin/python3
def search_replace(my_list, search, replace):
    return [((lambda x: replace if x == search else x)(x)) for x in my_list]
