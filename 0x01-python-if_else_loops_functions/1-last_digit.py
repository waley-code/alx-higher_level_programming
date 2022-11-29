#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
num = str(number)[-1]
print(f"Last digit of {number:d} is {num[-1]}", end=" ")
if int(num) > 5:
    print("and is greater than 5")
elif int(num) == 0:
    print("and is 0")
elif int(num) < 6 and int(num) != 0:
    print("and is less than 6 and not 0")
