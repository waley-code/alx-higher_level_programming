#!/usr/bin/python3
"""This is a rectangle module"""
from base import Base


class Rectangle(Base):
    """rectangle clase"""
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        type(self).__width = width
        type(self).__height = height
        type(self).__x = x
        type(self).__y = y

    def __str__(self):
        """prints strings of class"""
        x = "[{}] ({}) {}/{} - {}/{}"
        rN = type(self).__name__
        rId = self.id
        rX = self.__x
        rY = self.__y
        rW = self.__width
        rH = self.__height
        return x.format(rN, rId, rX, rY, rW, rH)

    @property
    def width(self):
        """width getter variable"""
        return self.__width
    
    @width.setter
    def width(self, arg):
        """width setter variable"""
        if type(arg) is not int:
            raise TypeError("width must be an integer")
        if arg <= 0:
            raise ValueError("width must be > 0")
        self.__width = arg
    
    @property
    def height(self):
        """height getter variable"""
        return self.__height
    
    @height.setter
    def height(self, arg):
        """height setter variable"""
        if type(arg) is not int:
            raise TypeError("height must be an integer")
        if arg <= 0:
            raise ValueError("height must be > 0")
        self.__height = arg
    
    @property
    def x(self):
        """x getter variable"""
        return self.__x
    
    @x.setter
    def x(self, arg):
        """x setter variable"""
        if type(arg) is not int:
            raise TypeError("x must be an integer")
        if arg < 0:
            raise ValueError("x must be >= 0")
        self.__x = arg

    @property
    def y(self):
        """y getter variable"""
        return self.__y
    
    @y.setter
    def y(self, arg):
        """y setter variable"""
        if type(arg) is not int:
            raise TypeError("y must be an integer")
        if arg < 0:
            raise ValueError("y must be >= 0")
        self.__y = arg
    
    def area(self):
        """returns rectangle area"""
        return self.__height * self.__width
    
    def display(self):
        """prints Rectangle instance with the character #"""
        for i in range(self.__height):
            print("{}".format(self.__x * " "), end="")
            for j in range(self.__width):
                print('#', end="")
            print()
    
    def update(self, *args, **kwargs):
        """assigns an argument to each attribute"""
        if args != None and args:
            x = []
            for i in args:
                x.append(i)
            if len(x) == 1:
                self.id = x[0]
            if len(x) == 2:
                self.id = x[0]
                self.__width = x[1]
            if len(x) == 3:
                self.id = x[0]
                self.__width = x[1]
                self.__height = x[2]
            if len(x) == 4:
                self.id = x[0]
                self.__width = x[1]
                self.__height = x[2]
                self.__x = x[3]
            if len(x) == 5:
                self.id = x[0]
                self.__width = x[1]
                self.__height = x[2]
                self.__x = x[3]
                self.__y = x[4]
        else:
            for key, value in kwargs.items():
                if key == "height":
                    self.__height = value
                if key == "width":
                    self.__width = value
                if key == "x":
                    self.__x = value
                if key == "y":
                    self.__y = value
                if key == "id":
                    self.id = value