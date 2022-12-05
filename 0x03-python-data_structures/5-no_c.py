#!/usr/bin/env python3
def no_c(my_string):
    str = ""
    if "c" in my_string or "C" in my_string:
        for i in my_string:
            if "c" == i or "C" == i:
                continue
            else:
                str += i
    else:
        return my_string
    return str
