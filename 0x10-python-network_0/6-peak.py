#!/usr/bin/python3
def find_peak(list_of_integers):
    """finds a peak in a list of unsorted integers"""
    if not list_of_integers:
        return None
    mid = len(list_of_integers) // 2
    if (mid == len(list_of_integers) - 1 or list_of_integers[mid] >= list_of_integers[mid + 1]) and (mid == 0 or list_of_integers[mid] >= list_of_integers[mid - 1]):
        return list_of_integers[mid]
    if mid != len(list_of_integers) - 1 and list_of_integers[mid + 1] > list_of_integers[mid]:
        return find_peak(list_of_integers[mid + 1:])
    return find_peak(list_of_integers[:mid])
