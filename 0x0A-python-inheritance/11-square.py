#!/usr/bin/python3
"""
===================================
module with class Square
===================================
"""
Rectangle = __import__('9-rectangle').Rectangle

class Square(Rectangle):
    """Square class that inherits from Square"""
    
    def __init__(self, size):
        super().__init__(size, size)
        self.integer_validator("size", size)
        self.__size = size

    def __str__(self):
        return "[{}] {}/{}".format(type(self).__name__, self.__size, self.__size)

    def area(self):
        """
            Calculates area of Square
        """
        return self.__size**2