from unittest import TestCase
from day18.solution import Expression

test_str = '1 + 2 * 3 + 4 * 5 + 6'


class TestSolution(TestCase):
    def test_expression(self):
        exp = Expression()
        exp.left = 2
        exp.right = 3
        exp.operator = '+'
        self.assertEqual(5, exp.value())
        exp.operator = '*'
        self.assertEqual(6, exp.value())
