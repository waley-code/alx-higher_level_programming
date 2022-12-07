#!/usr/bin/python3
def search_replace(my_list, search, replace):
    newG = []
    for i in my_list:
        if i == search:
            i = replace
        newG.append(i)
    return newG
