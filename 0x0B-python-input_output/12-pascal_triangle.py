#!/usr/bin/python3
"""Module of pascals triangle"""


def pascal_triangle(n):
    """function printing pascal triangle"""
    ax = [[1]]
    if n <= 0:
        return []
    x = [1]
    for row_num in range(n-1):
        previous = x[:]
        for k in range(row_num):
            x[k + 1] = previous[k] + previous[k + 1]
        x.append(1)
        ax.append(x[:])
    return ax
