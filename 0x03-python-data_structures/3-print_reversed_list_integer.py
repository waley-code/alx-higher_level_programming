#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    new_list = []
    i = 1
    while i <= len(my_list):
        new_list.append(my_list[-i])
        i = i + 1
    for j in range(len(new_list)):
        print("{:d}".format(int(new_list[j])))
