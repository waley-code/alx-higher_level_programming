#!/usr/bin/python3
def uniq_add(my_list=[]):
    s = []
    num = 0
    for i in my_list:
        if i not in s:
            s.append(i)
    for i in s:
        num += i
    return num
