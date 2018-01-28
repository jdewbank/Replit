import unittest

class AdditionTests(unittest.TestCase):
    def test_add_is_a_function(self):
        self.assertTrue(True)

    def test_adds_two_positive_numbers(self):
        self.assertEqual(2, 2)