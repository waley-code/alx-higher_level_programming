#!/usr/bin/python3
"""This module contains a class that inherits from
    another
"""


class MyList(list):
    """
        a class MyList that inherits from list,
        prints the list, but sorted (ascending sort)
    """
    def print_sorted(self):
        print(sorted(list(self)))