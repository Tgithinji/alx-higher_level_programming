#!/usr/bin/python3
""" test_base module """
import unittest
from models.base import Base


class BaseTestCase(unittest.TestCase):
    """
    Run unittests to test Base class
    """
    def setUp(self):
        self.b1 = Base()
        self.b2 = Base(20)

    def test_base_instance(self):
        """
        test instances of base
        """
        self.assertEqual(Base, type(self.b1))
        self.assertEqual(Base, type(self.b2))
        self.assertEqual(type(self.b1), type(self.b2))

    def test_nb_instance(self):
        """
        test that nb_instance attr is private
        """
        with self.assertRaises(AttributeError):
            print(self.b1.__nb_instances)
            print(self.b2.__nb_instances)

    def test_id_after_nb_instance(self):
        """
        tests id value after passing a value
        """
        b3 = Base()
        self.assertEqual(self.b1.id, b3.id - 1)
        self.assertEqual(20, self.b2.id)

    def test_id_int(self):
        """
        test id with integers and None
        """
        b3 = Base(None)
        self.assertEqual(self.b1.id, b3.id - 1)
        self.b1.id = 15
        self.assertEqual(15, self.b1.id)
        self.b2.id = 15
        self.assertEqual(15, self.b2.id)

    def test_id_str(self):
        """
        test id with strings
        """
        b3 = Base("Ted")
        self.assertEqual('Ted', b3.id)
        self.b1.id = "Ted"
        self.assertEqual(self.b1.id, b3.id)

    def test_id_data_types(self):
        """
        test id with different data structures
        """
        b_list = Base([1, 2])
        b_dict = Base({"one": 1, "two": 2})
        b_tuple = Base((1, 2))
        b_set = Base({1, 2})
        self.assertEqual([1, 2], b_list.id)
        self.assertEqual({"one": 1, "two": 2}, b_dict.id)
        self.assertEqual((1, 2), b_tuple.id)
        self.assertEqual({1, 2}, b_set.id)

    def test_id_bool(self):
        """
        test instances with boolean values
        """
        b_true = Base(True)
        b_false = Base(False)
        self.assertTrue(b_true.id)
        self.assertFalse(b_false.id)

    def test_multiple_args(self):
        """
        Check if typeerror will be raised when we have
        excess arguments
        """
        with self.assertRaises(TypeError):
            b = Base(12, 10)

if __name__ == '__main__':
    unittest.main()
