#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
from models.base import Base

class TestBase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.b1 = Base()
        cls.b2 = Base()
        cls.b3 = Base()
        cls.b4 = Base(69)

    def test_init(self):
        """Test id auto assignment"""
        self.assertEqual(self.b1.id, 1)
        self.assertEqual(self.b2.id, 2)
        self.assertEqual(self.b3.id, 3)

    def test_passed_id(self):
        """Test that it saves passed id"""
        self.assertEqual(self.b4.id, 69)


    def test_to_json(self):
        """Test json to string"""
        self.assertEqual(Base.to_json_string([]), '[]')
        self.assertEqual(Base.to_json_string(None), '[]')
        self.assertEqual(Base.to_json_string([{'id': 69}]), '[{"id": 69}]')

    def test_from_json(self):
        """Test string to json"""
        self.assertEqual(Base.from_json_string('[{"id": 69}]'), [{'id': 69}])
        self.assertEqual(Base.from_json_string(None), [])
        self.assertEqual(Base.from_json_string("[]"), [])
