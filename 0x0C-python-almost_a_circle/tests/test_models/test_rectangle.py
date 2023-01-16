#!/usr/bin/python3
"""Rectangle class tests module"""

import unittest
from models.base import Base
from models.rectangle import Rectangle

class test_rectangle_class(unittest.TestCase):
    """Tseting for the rectangle init method"""
    def setUp(self):
        Base.__nb_objects = 0


    def test_excess_arguments(self):
        """Testing with excess args
            expecting typeError
        """  
        with self.assertRaises(TypeError):
            Rectangle(5, 6, 7, 1, 3, 9)

    def test_withEmpty_arg(self):
        """Testing with empty args
            expecting typeError
        """
        with self.assertRaises(TypeError):
            Rectangle()

    def test_withSingle_argument(self):
        """Testing with single args
            expecting typeError
        """       
        with self.assertRaises(TypeError):
            Rectangle(4)
    

    def test_Rectangle_widthAndHeight(self):
        """
        Testing rectangle wdith and Heights
        """
        self.assertEqual(Rectangle(3, 3, 1).id, 7)
        self.assertEqual(Rectangle(5, 1, 1).id, 8)

    def test_Rectangle_withNoId(self):
        """
        testing rectangle without id
        """
        self.assertEqual(Rectangle(5, 6, 3, 3, 4).id, 4)
        self.assertEqual(Rectangle(7, 3, 1, 4, 5).id, 5)

    def test_Rectangle_withId(self):
        """
        testing rectangle with Id
        """
        self.assertEqual(Rectangle(2, 4, 1, 2, 4).id, 4)
        self.assertEqual(Rectangle(4, 2, 2, 1, 2).id, 2)

    def test_width_setAndGet(self):
        """
        testing the get and set method
        
        """
        x = Rectangle(2, 3, 5, 2)
        with self.assertRaises(AttributeError):
            x.__width
        self.assertEqual(x.width, 2)
        x.width = 12
        self.assertEqual(x.width, 12)

    def test_run_update_id_widthHeight_x(self):
        """
        Testing update methods
        """
        x = Rectangle(3, 4, 1, 3, 42)
        x.update(32, 10, 20, 50)
        self.assertEqual(str(x), "[Rectangle] (32) 50/3 - 10/20")
    
    def test_dictionary_withBasic_argument(self):
        """
            Testing with basic args expecting error
        """
        with self.assertRaises(TypeError):
            Rectangle(4, 5, 3, 2, 34).to_dictionary(34)

    def test_run_update_id_widthHeight_x_y(self):
        """
        Testing all parameteras of update method
        """
        x = Rectangle(2, 3, 5, 3, 42)
        x.update(32, 10, 20, 52, 32)
        self.assertEqual(str(x), "[Rectangle] (32) 52/32 - 10/20")



if __name__ == "__main__":
    unittest.main()