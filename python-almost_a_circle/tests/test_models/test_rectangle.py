#!/usr/bin/python3
"""Unittest for Rectangle Class"""

import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.r1 = Rectangle(1, 2, 3, 4)
        cls.r2 = Rectangle(1, 2)
        cls.r3 = Rectangle(1, 2, 3)
    
    def test_normal(self):
        self.assertEqual(self.r1.width, 1)
        self.assertEqual(self.r1.height, 2)
        self.assertEqual(self.r1.x, 3)
        self.assertEqual(self.r1.y, 4)
        self.assertEqual(self.r2.width, 1)
        self.assertEqual(self.r2.height, 2)
        self.assertEqual(self.r3.width, 1)
        self.assertEqual(self.r3.height, 2)
        self.assertEqual(self.r3.x, 3)
