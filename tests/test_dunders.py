import unittest

from src.dunders.dunders_minimal_case import MyObject


class TestDundersMinimalCase(unittest.TestCase):
    def test_add_returns_new_object_with_sum(self):
        a = MyObject(1)
        b = MyObject(2)
        c = a + b
        self.assertIsInstance(c, MyObject)
        self.assertEqual(1, a.value)
        self.assertEqual(2, b.value)
        self.assertEqual(3, c.value)


if __name__ == '__main__':
    unittest.main()