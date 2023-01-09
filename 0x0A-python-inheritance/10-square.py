#!/usr/bin/python3
"""
===================================
module with class Square
===================================
"""
Rectangle = __import__('9-rectangle').Rectangle

class Square(Rectangle):
    """Square class that inherits from BaseGeometry"""
    
    def __init__(self, size):
        Rectangle.__init__(self, size, size)
        self.integer_validator("size", size)
        self.__size = size
    
    def area(self):
        """
            Calculates area of Square
        """
        return self.__size **2
