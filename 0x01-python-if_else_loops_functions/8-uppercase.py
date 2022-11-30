#!/usr/bin/python3
def uppercase(str):
    stri = ""
    for i in str:
        if i >= 'a' and i <= 'z':
            stri += "{:c}".format(ord(i)-32)
        else:
            stri += "{}".format(i)
    print(stri, end="\n")
