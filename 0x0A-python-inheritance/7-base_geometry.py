#!/usr/bin/python3
"""
    Contains a class BaseGeometry which
     inherit fr object
"""


class BaseGeometry(object):
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
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))