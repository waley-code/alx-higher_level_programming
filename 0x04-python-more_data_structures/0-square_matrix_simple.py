#!/usr/bin/python3
def square_matrix_simple(x=[]):
    lis = []
    for i in x:
        l1 = []
        for j in i:
            l1.append(j**2)
        lis.append(l1)
    return lis
