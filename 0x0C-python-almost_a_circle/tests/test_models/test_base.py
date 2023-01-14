#!/usr/bin/python3
"""Tests module"""


import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBaseMethods(unittest.TestCase):
  """testing class"""

  def test_upper(self):
    """tests upper"""
    self.assertEqual(Base().id, 1)
