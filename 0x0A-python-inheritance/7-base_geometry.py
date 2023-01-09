#!/usr/bin/python3
"""
    Contains  an empty class BaseGeometry.
"""


class BaseGeometry:
    """ a BaseGeometry class"""
    def area(self):
        """Raises an exception abot area() method"""
        raise Exception("area() is not implemented")
    
    def integer_validator(self, name, value):
        """Method that validates value"""
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(name))