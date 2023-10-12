#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    ordered_list = list(a_dictionary.keys())
    ordered_list.sort()
    for x in ordered_list:
        print("{}:{}".format(x, a_dictionary.get(x)))
