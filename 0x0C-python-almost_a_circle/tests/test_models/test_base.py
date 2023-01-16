#!/usr/bin/python3
"""Base class tests module"""


import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBaseId(unittest.TestCase):
    """testing id"""

    def test_mixture_grp_id(self):
        """tESTS FOR A MIXTURE OF IDS"""
        self.assertEqual(Base(None).id, 1)
        self.assertEqual(Base(None).id, 2)
        self.assertEqual(Base(8).id, 8)
        self.assertEqual(Base(None).id, 3)
        self.assertEqual(Base().id, 4)
        self.assertEqual(Base(-7).id, -7)

    def test_instantiationWitArg(self):
        """tests instatiation with argument"""
        self.assertEqual(Base(3).id, 3)

    def test_idNegative_Int(self):
        """Tests for negative integer"""
        self.assertEqual(Base(-6).id, -6)

    def test_instantiationWitString(self):
        """tests instatiation with string"""
        with self.assertRaises(TypeError):
            Base("ht")


class TestBaseToString(unittest.TestCase):
    """test for json to strng method"""

    def test_base_to_json_string_withMany_param(self):
        """Check for type error with multi args"""
        with self.assertRaises(TypeError):
            Base.to_json_string([], 78)

    def test_json_to_string(self):
        """Tests json to string func"""
        r1 = Rectangle(10, 7, 2, 8)
        dictionary = r1.to_dictionary()
        self.assertEqual(sorted(
            dictionary), sorted(
                {'x': 2, 'width': 10, 'id': 1, 'height': 7, 'y': 8}))

    def test_to_json_string_withVacant_lists(self):
        """testing with an empty list args"""
        self.assertEqual(Base.to_json_string([]), '[]')

    def test_to_json_string_dictAttr_rectangle(self):
        """Tests for the basic dictionary arttributes"""
        xDict = [Rectangle(1, 3, 5, 6, 82).to_dictionary()]
        self.assertTrue(len(Base.to_json_string(xDict)) == 53)


class Test_BaseClass_create(unittest.TestCase):
    """Test for the create method in Base class"""

    def test_BaseCreate_rectangle(self):
        """Still testing the create method"""
        y = {'id': 3, 'height': 4, 'x': 1, 'y': 2, 'width': 2}
        x = Rectangle.create(**y).to_dictionary()
        self.assertDictEqual(x, y)

    def test_create_basic_square(self):
        """Test for create method"""
        y = {'y': 6, 'id': 56, 'size': 9, 'x': 1}
        x = Square.create(**y).to_dictionary()
        self.assertDictEqual(x, y)


if __name__ == "__main__":
    unittest.main()
