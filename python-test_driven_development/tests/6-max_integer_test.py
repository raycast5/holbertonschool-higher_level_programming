#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_max(self):
        self.assertEqual(max_integer([10, 2, 5, 15, 7, 20, 2]), 20)
        self.assertEqual(max_integer([10, 2, 5, 15.5, 7, 4, 2]), 15.5)
        self.assertEqual(max_integer([10, 2, 5, -15, 7, -20, 2]), 10)
        self.assertEqual(max_integer([10, 2, 5, 15, 7, 2, 20]), 20)
        self.assertEqual(max_integer([2]), 2)

        
    def test_empty(self):
        self.assertIsNone(max_integer([]))
