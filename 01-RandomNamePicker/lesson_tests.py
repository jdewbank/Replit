class AdditionTests(unittest.TestCase):
    def test_add_is_a_function(self):
        self.assertTrue(callable(add))

    def test_adds_two_positive_numbers(self):
        self.assertEqual(add(1, 1), 2)