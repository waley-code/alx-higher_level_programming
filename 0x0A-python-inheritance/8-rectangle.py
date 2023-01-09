#!/usr/bin/python3
"""
    This module creates a class rectangle
"""
class BaseGeometry:
    """ a BaseGeometry class inherit from object"""

    def area(self):
        """
            Raises an exception about an area 
            method
        """
        raise Exception("area() is not implemented")
    
    def integer_validator(self, name, value):
        """Method that validates value"""

        if type(value) is not int:
            raise TypeError("{} must be an integer".format("height"))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
        return

class Rectangle(BaseGeometry):
    def __init__(self, width, height):
        BaseGeometry.integer_validator(self, width, height)
        type(self).__width = width
        type(self).__height = height