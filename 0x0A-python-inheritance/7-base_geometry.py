#!/usr/bin/python3
"""
    Contains an empty class BaseGeometry.
"""


class BaseGeometry:
    """ a BaseGeometry class"""
    def area(self):
        """Raises an exception abot area() method"""
        raise Exception("area() is not implemented")
    
    def integer_validator(self, name, value):
        """Method that validates value"""
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")