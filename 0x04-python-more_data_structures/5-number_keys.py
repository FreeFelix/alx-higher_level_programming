#!/usr/bin/python3

def number_keys(a_dictionary):
    x = 0
    list_keys = list(a_dictionary.keys())
    for y in list_keys:
        x += 1
    return x
