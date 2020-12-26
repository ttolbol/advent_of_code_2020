from unittest import TestCase
from day18.solution import shunting_yard, evaluate_rpn

test_str1 = '1 + 2 * 3 + 4 * 5 + 6'
test_str2 = '5 + (8 * 3 + 9 + 3 * 4 * 3)'
rpn_str1 = '12+3*4+5*6+'
rpn_str2 = '583*9+3+4*3*+'


class TestSolution(TestCase):
    def test_shunting_yard(self):
        self.assertEqual(rpn_str1, shunting_yard(test_str1))
        self.assertEqual(rpn_str2, shunting_yard(test_str2))

    def test_evaluate_rpn(self):
        self.assertEqual(71, evaluate_rpn(rpn_str1))
        self.assertEqual(437, evaluate_rpn(rpn_str2))
