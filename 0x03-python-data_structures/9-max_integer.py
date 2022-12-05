#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return None
    newList = my_list.copy()
    newList.sort()
    return newList[-1]
