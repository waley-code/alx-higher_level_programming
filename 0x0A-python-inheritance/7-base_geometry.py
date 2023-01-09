#!/usr/bin/python3
"""
    Contains an empty class BaseGeometry.
"""


class BaseGeometry:
    """ a BaseGeometry class"""
    def area(self):
        """
            Raises an exception abot area 
            method
        """
        raise Exception("area() is not implemented")
    
    def integer_validator(self, name, value):
        """Method that validates value"""

        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))