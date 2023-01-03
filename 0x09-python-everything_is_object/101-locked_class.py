#!/usr/bin/python3
class LockedClass:
    def __setattr__(self, attribute, value):
        if attribute == "first_name":
            self.__dict__[attribute] = value
        else:
            x = "'LockedClass' object has no attribute '" + attribute + "'"
            raise AttributeError(x)
