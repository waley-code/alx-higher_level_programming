#!/usr/bin/python3
"""
    This is a module containing a class that defines a class square.
"""
class Square:
    """
        This class defines class when instantiated.
    """
    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes private size value
        """
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """
            returns a private attribute of class.
        """
        return self.__size

    @property
    def position(self):
        """
            returns a private attribute of class.
        """
        return self.__position

    @size.setter
    def size(self, value):
        """
            raise ValueError if size < 0
            raise TypeError if size != int
        """
        if (type(value) != int):
            """
                check for type inputed
            """
            raise TypeError("size must be an integer")
        if ((value < 0)):
            """
                check for type is ==int inputed
            """
            raise ValueError("size must be >= 0")
        self.__size = value

    @position.setter
    def position(self, value):
        """
            raise ValueError if size < 0
            raise TypeError if size != int
        """
        if (type(value) != (type((9, 5))) or len(value) != 2):
            for i in value:
                if i < 0:
                    """
                        check for type inputed
                    """
                    raise TypeError("position must be a tuple of 2 positive integers")
    def area(self):
        """
            Calculates and returns the current square area
        """
        return self.__size**2

    def my_print(self):
        """
            prints in stdout the square with the character #.
        """
        if (self.__size == 0):
            print()
        else:
            for r in range(self.__position[1]):
                print()
            for i in range(self.__size):
                print("{}{}".format(self.__position[0] * "_", self.__size * "#") )

my_square_1 = Square(3)
my_square_1.my_print()

print("--")

my_square_2 = Square(3, (1, 1))
my_square_2.my_print()

print("--")

my_square_3 = Square(3, (3, 0))
my_square_3.my_print()

print("--")