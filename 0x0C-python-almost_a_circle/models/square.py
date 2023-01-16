#!/usr/bin/python3
"""Square module containing square class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """square inherits bfrom rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        """square constructor"""
        super().__init__(size, size, x, y, id)
        self.width = size
        self.height= size

    def __str__(self):
        """string printer"""
        super().__str__()
        x = "[{}] ({}) {}/{} - {}"
        rN = type(self).__name__
        rId = self.id
        rX = self.x
        rY = self.y
        rW = self.width
        rH = self.width
        return x.format(rN, rId, rX, rY, rH)

    @property
    def size(self):
        """width getter variable"""
        return self.width
    
    @size.setter
    def size(self, arg):
        """size setter variable"""
        if type(arg) is not int:
            raise TypeError("width must be an integer")
        if arg <= 0:
            raise ValueError("width must be > 0")
        self.width = arg
        self.height = arg
    
    
    def update(self, *args, **kwargs):
        """update method"""
        if args != None and args:
            x = []
            for i in args:
                x.append(i)
            if len(x) == 1:
                self.id = x[0]
            if len(x) == 2:
                self.id = x[0]
                self.size= x[1]
            if len(x) == 3:
                self.id = x[0]
                self.size= x[1]
                self.x = x[2]
            if len(x) == 4:
                self.id = x[0]
                self.size= x[1]
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
        """converts to dictionary"""
        id = getattr(self, 'id')
        size = getattr(self, 'size')
        x = getattr(self, 'x')
        y = getattr(self, 'y')
        return {"id" : id, "y" : y, "x" : x, "size" : size}