#!/usr/bin/python3
"""Square module containing square class"""
from rectangle import Rectangle


class Square(Rectangle):
    """square inherits bfrom rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        """square constructor"""
        super().__init__(size, size, x, y, id)
        self.size = size
    def __str__(self):
        return super().__str__()

    @property
    def size(self):
        """width getter variable"""
        return self.width
    
    @size.setter
    def size(self, arg):
        """size setter variable"""
        self.width = arg
        self.height = arg
    
    def update(self, *args, **kwargs):
        if args != None and args:
            x = []
            for i in args:
                x.append(i)
            if len(x) == 1:
                self.id = x[0]
            if len(x) == 2:
                self.id = x[0]
                self.size = x[1]
            if len(x) == 3:
                self.id = x[0]
                self.size = x[1]
                self.x = x[2]
            if len(x) == 4:
                self.id = x[0]
                self.size = x[1]
                self.x = x[2]
                self.y = x[3]
        else:
            for key, value in kwargs.items():
                if key == "size":
                    self.size = value
                if key == "x":
                    self.x = value
                if key == "y":
                    self.y = value
                if key == "id":
                    self.id = value

    def to_dictionary(self):
        """square to dictionary"""
        