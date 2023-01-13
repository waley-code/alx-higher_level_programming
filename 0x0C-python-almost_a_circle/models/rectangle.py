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

        @property
        def width(self):
            """width getter variable"""
            return self.__width
        
        @width.setter
        def width(self, arg):
            """width setter variable"""
            self.__width = arg
        
        @property
        def height(self):
            """height getter variable"""
            return self.__height
        
        @height.setter
        def height(self, arg):
            """height setter variable"""
            self.__height = arg
        
        @property
        def x(self):
            """x getter variable"""
            return self.__x
        
        @x.setter
        def x(self, arg):
            """x setter variable"""
            self.__x = arg

        @property
        def y(self):
            """y getter variable"""
            return self.__y
        
        @y.setter
        def x(self, arg):
            """y setter variable"""
            self.__y = arg