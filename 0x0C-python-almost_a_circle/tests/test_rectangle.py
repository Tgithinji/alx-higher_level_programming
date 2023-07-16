#!/usr/bin/python3
"""
This is the module to test_rectangle
"""
import unittest
from io import StringIO
from unittest.mock import patch
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
        self.assertEqual(12, r1.id)

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


class TestSetterGetter(unittest.TestCase):
    """
    Tests a rectangles setter and getter methods
    """
    def test_get_width(self):
        r = Rectangle(5, 2)
        self.assertEqual(5, r.width)

    def test_set_width(self):
        r = Rectangle(5, 2)
        r.width = 7
        self.assertEqual(7, r.width)

    def test_get_height(self):
        r = Rectangle(5, 2)
        self.assertEqual(2, r.height)

    def test_set_height(self):
        r = Rectangle(5, 2)
        r.height = 7
        self.assertEqual(7, r.height)

    def test_get_x(self):
        r = Rectangle(5, 2, 9)
        self.assertEqual(9, r.x)

    def test_set_x(self):
        r = Rectangle(5, 2, 9, 8)
        r.x = 7
        self.assertEqual(7, r.x)

    def test_set_y(self):
        r = Rectangle(5, 2, 9, 8)
        self.assertEqual(8, r.y)

    def test_set_y(self):
        r = Rectangle(5, 2, 9, 8)
        r.y = 70
        self.assertEqual(70, r.y)

    def test_width_exception(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(None, 2)
            Rectangle("12", 2)
            Rectangle(2.2, 2)
            Rectangle([1, 2], 2)
            Rectangle({"a": 1, "b": 2}, 2)
            Rectangle((1, 2), 2)
            Rectangle({1, 2}, 2)

        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(-1, 2)
            Rectangle(0, 2)

    def test_height_exception(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(2, None)
            Rectangle(2, "12")
            Rectangle(2, 2.2)
            Rectangle(2, [1, 2])
            Rectangle(2, {'a': 1, 'b': 2})
            Rectangle(2, (1, 2))
            Rectangle(2, {1, 2})
            Rectangle(2, True)

        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(1, -2)
            Rectangle(2, 0)

    def test_x_exception(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(2, 2, None)
            Rectangle(2, 4, "12")
            Rectangle(2, 5, 2.2)
            Rectangle(2, 5, [1, 2])
            Rectangle(2, 5, {'a': 1, 'b': 2})
            Rectangle(2, 5, (1, 2))
            Rectangle(2, 5, {1, 2})
            Rectangle(2, 5, True)

        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Rectangle(1, 5, -2)

    def test_y_exception(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(2, 2, 4, None)
            Rectangle(2, 4, 4, "12")
            Rectangle(2, 5, 4, 2.2)
            Rectangle(2, 5, 4, [1, 2])
            Rectangle(2, 5, 4, {'a': 1, 'b': 2})
            Rectangle(2, 5, 4, (1, 2))
            Rectangle(2, 5, 4, {1, 2})
            Rectangle(2, 5, 4, True)

        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Rectangle(1, 5, 3, -2)


class TestaAreaDisplay(unittest.TestCase):
    def test_area(self):
        r = Rectangle(3, 2)
        r2 = Rectangle(8, 7, 0, 0, 12)
        self.assertEqual(6, r.area())
        self.assertEqual(56, r2.area())

    def test_big_number_area(self):
        r = Rectangle(5555555, 5555555)
        self.assertEqual(30864191358025, r.area())

    def test_area_with_changed_attributes(self):
        r = Rectangle(3, 2)
        r.width = 10
        r.height = 5
        self.assertEqual(50, r.area())

    def test_exception_with_extra_args(self):
        with self.assertRaises(TypeError):
            r = Rectangle(3, 2)
            r.area(1)

    def test_display_to_stdout(self):
        with patch('sys.stdout', new=StringIO()) as f:
            r = Rectangle(3, 2)
            r.display()
            self.assertEqual(f.getvalue(), "###\n###\n")

    def test_display_with_args(self):
        with self.assertRaises(TypeError):
            r = Rectangle(3, 2)
            r.display(1)

    def test_str_representation(self):
        r = Rectangle(3, 2)
        expected_out = "[Rectangle] ({}) 0/0 - 3/2".format(r.id)
        self.assertEqual(expected_out, r.__str__())

    def test_str_with_x(self):
        r = Rectangle(3, 2, 5)
        expected_out = "[Rectangle] ({}) 5/0 - 3/2".format(r.id)
        self.assertEqual(expected_out, r.__str__())

    def test_str_with_xy(self):
        r = Rectangle(3, 2, 5, 6)
        expected_out = "[Rectangle] ({}) 5/6 - 3/2".format(r.id)
        self.assertEqual(expected_out, r.__str__())

    def test_str_with_id(self):
        r = Rectangle(2, 5, 3, 2, 12)
        expected_out = "[Rectangle] (12) 3/2 - 2/5"
        self.assertEqual(expected_out, r.__str__())

    def test_str_with_args(self):
        with self.assertRaises(TypeError):
            r = Rectangle(3, 2)
            r.__str__(1)


if __name__ == "__main__":
    unittest.main()
