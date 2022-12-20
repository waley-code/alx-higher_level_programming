#!/usr/bin/python3
#!/usr/bin/python3
"""
    This is a module containing a class that defines a class square.
"""
class Square:
    """
        This class defines class when instantiated.
    """
    def __init__(self, size=0):
        """
        Initializes private size value
        raise ValueError if size < 0
        raise TypeError if size != int
        """
        if (type(size) != int):
            """
                check for type inputed
            """
            raise TypeError("size must be an integer")
        if ((size < 0)):
            """
                check for type is ==int inputed
            """
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
            Calculates and returns the current square area
        """
        return self.__size**2