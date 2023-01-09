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
        super().__init__(size, size)
        self.integer_validator("size", size)
        self.__size = size


s = Square(13)

print(s)
print(s.area())