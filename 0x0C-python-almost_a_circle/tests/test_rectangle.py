#!/usr/bin/python3
"""
This is the module to test_rectangle
"""
import unittest
from models.base import Base
from models.rectangle import Rectangle


class testRectangle(unittest.TestCase):
    """
    This are unittests to test a Rectangle instances
    """

    def test_rectangle_instances(self):
        r = Rectangle(10, 2)
        r1 = Rectangle(10, 2, 0, 0, 12)
        self.assertTrue(isinstance(r1, Base))
        self.assertEqual(type(r), type(r))

    def test_id(self):
        r = Rectangle(3, 4)
        r1 = Rectangle(10, 2, 0, 0, 12)
        r2 = Rectangle(10, 2)
        self.assertEqual(r.id, r2.id - 1)
        self.assertEqual(12, r2.id)

    def test_with_little_args(self):
        with self.assertRaises(TypeError):
            Rectangle()
            Rectangle(1)

    def test_many_args(self):
        with self.assertRaises(TypeError):
            Rectangle(10, 2, 0, 0, 12, 3)

    def test_private_attributes(self):
        with self.assertRaises(AttributeError):
             r = Rectangle(10, 2)
             print(r.__width)
             print(r.__height)
             print(r.__x)
             print(r.__y) 


if __name__ == "__main__":
    unittest.main()
