import io
import unittest
from contextlib import redirect_stdout

from src.decorators.decorator_example import my_decorator, do_twice
from src.decorators.inner_outer_func import (
    outer_func,
    outer_func_2,
    outer_func_3,
    outer_func_4,
)
from src.decorators.common_decorators import Square


class TestDecorators(unittest.TestCase):
    def test_my_decorator_prints_before_and_after(self):
        out = io.StringIO()
        calls = []

        def greet():
            calls.append('called')
            print("Hello")

        wrapped = my_decorator(greet)
        with redirect_stdout(out):
            wrapped()
        self.assertEqual(['called'], calls)
        self.assertEqual("Before function\nHello\nAfter function\n", out.getvalue())

    def test_do_twice_calls_function_twice_with_args(self):
        calls = []

        def add_to_list(x, y=0):
            calls.append(x + y)

        wrapped = do_twice(add_to_list)
        wrapped(2, y=3)
        self.assertEqual([5, 5], calls)

    def test_outer_func_prints_captured_value(self):
        out = io.StringIO()
        fn = outer_func()
        with redirect_stdout(out):
            fn()
        self.assertEqual("1\n", out.getvalue())

    def test_outer_func_2_prints_captured_value(self):
        out = io.StringIO()
        fn = outer_func_2()
        with redirect_stdout(out):
            fn()
        self.assertEqual("1\n", out.getvalue())

    def test_outer_func_3_nonlocal_increment(self):
        out = io.StringIO()
        fn = outer_func_3()
        with redirect_stdout(out):
            fn()
        self.assertEqual("2\n", out.getvalue())

    def test_outer_func_4_list_mutation(self):
        out = io.StringIO()
        fn = outer_func_4()
        with redirect_stdout(out):
            fn()
        self.assertEqual("[1]\n", out.getvalue())

    def test_square_properties_and_methods(self):
        out = io.StringIO()
        s = Square()
        with redirect_stdout(out):
            s.side = 4
            side_value = s.side
        # Property prints messages; assert they were printed in order
        self.assertIn("Setting side\nGetting side\n", out.getvalue())
        self.assertEqual(4, side_value)
        # Area and perimeter should use the property (which prints again if accessed)
        area = s.area()
        perimeter = s.perimeter()
        self.assertEqual(16, area)
        self.assertEqual(16, perimeter)
        self.assertEqual("square", s.get_type())


if __name__ == '__main__':
    unittest.main()
