#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    try:
        newlist = []
        n = 0
        for i in range(list_length):
            if (my_list_1[i] and my_list_2[i]):
                if (isinstance(my_list_1[i], (int, float)) and isinstance(my_list_2[i], (int, float))):
                    if (my_list_1[i] == 0 or my_list_2[i] == 0):
                        n += 1
                        newlist.append(0)
                        print("division by 0")
                    else:
                        n += 1
                        result = my_list_1[i] / my_list_2[i]
                        newlist.append(result)
                elif not (isinstance(my_list_1[i], (int, float)) and isinstance(my_list_2[i], (int, float))):
                    n += 1
                    newlist.append(0)
                    print("wrong type")
            if (not my_list_1[i]):
                newlist.append(0)
            if (not my_list_2[i]):
                print("division by 0")
                newlist.append(0)
    except IndexError:
        n += 1
        newlist.append(0)
        print("out of range")
    finally:
        return newlist