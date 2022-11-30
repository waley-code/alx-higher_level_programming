#!/usr/bin/python3
for i in range(97, 123):
    if f"{i:c}" == 'q' or f"{i:c}" == 'e':
         continue
    else:
         print("{:c}".format(i), end="")
