#!/usr/bin/python3
"""
===================================
module with class Rectangle
===================================
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    """Rectangle class that inherits from BaseGeometry"""

    def __str__(self):
        return "[{}] {}/{}".format(type(self).__name__, self.__width, self.__height)
    
    def __init__(self, width, height):
        super.__init__()
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
    
    def area(self):
        """
            Calculates area of rectangle
        """
        return self.__height * self.__width