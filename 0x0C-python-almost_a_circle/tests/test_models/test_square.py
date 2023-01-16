#!/usr/bin/python3
"""Rectangle class tests module"""

import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class test_square_class(unittest.TestCase):
    """Tseting for the square init method"""

    def test_return_y_value(self):
        """
            Testing the y arg
        """
        self.assertEqual(Square(4, 4, 4).y, 4)

    def test_return_width_value(self):
        """
            Testing the width arg
        """
        self.assertEqual(Square(4, 4, 4).width, 4)

    def test_return_x_value(self):
        """
            Testing the x arg
        """
        self.assertEqual(Square(5, 3, 5).x, 3)

    def test_return_height_value(self):
        """
             Testing the height arg
        """
        self.assertEqual(Square(2, 1, 2).height, 2)

    def test_with_no_arg(self):
        """
            Testing square without args
        """
        with self.assertRaises(TypeError):
            Square()

    def test_geting_size_val(self):
        """
            Testing the get size for return value
        """
        sqr = Square(4, 2, 4)
        self.assertEqual(Square(4, 2, 4).size, 4)
        sqr.size = 30
        self.assertEqual(sqr.size, 30)

    def test_required_val_square(self):
        """
            Testing square with required field
        """
        self.assertEqual(Square(8).id, 10)
