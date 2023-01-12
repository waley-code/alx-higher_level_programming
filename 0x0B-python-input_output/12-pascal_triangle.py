#!/usr/bin/python3
"""Module of pascals triangle"""


def pascal_triangle(n):
    if n <= 0:
        return list()
    x = [1]
    for row_num in range(n):
        print(x, end="")
        print()
        previous = x[:]
        for k in range(row_num):
            x[k + 1] = previous[k] + previous[k + 1]
        x.append(1)