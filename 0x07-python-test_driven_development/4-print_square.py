#!/usr/bin/python3
"""This module creates a square"""
def print_square(size):
    """This function creates a square"""
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for index in range(size):
        print("x" * size)