#!/usr/bin/python3
"""
This is the "Rectangle"  module.
This module provides a simple Rectangle class.
"""


class Rectangle:
    """ defines a rectangle """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initializes width"""
        Rectangle.number_of_instances += 1
        self.width = width
        self.height = height

    def __str__(self):
        """return informal string"""
        acc = ""
        if self.__height == 0 or self.__width == 0:
            return ""
        for i in range(self.__height):
            acc += "{}".format(str(self.print_symbol) * self.__width)
            if i is not self.__height - 1:
                acc += "\n"
        return acc

    def __repr__(self):
        """return formal string"""
        return "Rectangle({},{})".format(self.__width, self.__height)

    def __del__(self):
        """Bye rectangle... upon del && decrease count"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @property
    def width(self):
        """returns width"""
        return self.__width

    @property
    def height(self):
        """returns height"""
        return self.__height

    @width.setter
    def width(self, value):
        """sets width private property"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @height.setter
    def height(self, value):
        """sets height private property"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """returns area"""
        return self.__height * self.__width

    def perimeter(self):
        """returns perimeter"""
        if self.height == 0 or self.width == 0:
            return 0
        return 2 * (self.__height + self.__width)
    
    @classmethod
    def square(cls, size=0):
        return Rectangle(size, size)

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        elif not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2