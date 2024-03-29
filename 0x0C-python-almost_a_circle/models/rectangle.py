#!/usr/bin/python3
"""This is a rectangle module"""
from models.base import Base


class Rectangle(Base):
    """rectangle clase"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """instatiation init method"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def __str__(self):
        """prints strings of class"""
        x = "[{}] ({}) {}/{} - {}/{}"
        rN = type(self).__name__
        rId = self.id
        rX = self.x
        rY = self.y
        rW = self.width
        rH = self.height
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
        return self.height * self.width
    
    def display(self):
        """prints Rectangle instance with the character #"""
        for i in range(self.height):
            print("{}".format(self.x * " "), end="")
            for j in range(self.width):
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
                self.width = x[1]
            if len(x) == 3:
                self.id = x[0]
                self.width = x[1]
                self.height = x[2]
            if len(x) == 4:
                self.id = x[0]
                self.width = x[1]
                self.height = x[2]
                self.x = x[3]
            if len(x) == 5:
                self.id = x[0]
                self.width = x[1]
                self.height = x[2]
                self.x = x[3]
                self.y = x[4]
        else:
            for key, value in kwargs.items():
                if key == "height":
                    type(self).height = value
                if key == "width":
                    type(self).width = value
                if key == "x":
                    type(self).x = value
                if key == "y":
                    type(self).y = value
                if key == "id":
                    self.id = value

    def to_dictionary(self):
        """converts to dictionary"""
        id = getattr(self, 'id')
        width = getattr(self, 'width')
        height = getattr(self, 'height')
        x = getattr(self, 'x')
        y = getattr(self, 'y')
        return {"id" : id, "y" : y, "x" : x, "width" : width, "height" : height}