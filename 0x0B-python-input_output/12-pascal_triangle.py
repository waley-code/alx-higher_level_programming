#!/usr/bin/python3
"""Module of pascals triangle"""


def pascal_triangle(n):
    ax = []
    if n <= 0:
        return ax
    x = [1]
    for row_num in range(n):
        ax.append(x[:])
        previous = x[:]
        for k in range(row_num):
            x[k + 1] = previous[k] + previous[k + 1]
        x.append(1)
    return ax
