from unittest import TestCase
from day18.solution import shunting_yard, evaluate_rpn

test_str1 = '1 + 2 * 3 + 4 * 5 + 6'
test_str2 = '5 + (8 * 3 + 9 + 3 * 4 * 3)'
rpn_str1 = '12+3*4+5*6+'
rpn_str1_prec = '12+34+*56+*'
rpn_str2 = '583*9+3+4*3*+'
rpn_str2_prec = '5839+3+*4*3*+'

test_strings = {
    '1 + (2 * 3) + (4 * (5 + 6))': 51,
    '2 * 3 + (4 * 5)': 26,
    '5 + (8 * 3 + 9 + 3 * 4 * 3)': 437,
    '5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))': 12240,
    '((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2': 13632
}

test_strings_prec = {
    '1 + (2 * 3) + (4 * (5 + 6))': 51,
    '2 * 3 + (4 * 5)': 46,
    '5 + (8 * 3 + 9 + 3 * 4 * 3)': 1445,
    '5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))': 669060,
    '((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2': 23340
}

operator_precedence = {'+': 2, '*': 1}


class TestSolution(TestCase):
    def test_shunting_yard(self):
        self.assertEqual(rpn_str1, shunting_yard(test_str1))
        self.assertEqual(rpn_str2, shunting_yard(test_str2))

    def test_shunting_yard_precedence(self):
        self.assertEqual(rpn_str1_prec, shunting_yard(test_str1, operator_precedence))
        self.assertEqual(rpn_str2_prec, shunting_yard(test_str2, operator_precedence))

    def test_evaluate_rpn(self):
        self.assertEqual(71, evaluate_rpn(rpn_str1))
        self.assertEqual(437, evaluate_rpn(rpn_str2))

    def test_integrated(self):
        for test_str, val in test_strings.items():
            self.assertEqual(val, evaluate_rpn(shunting_yard(test_str)))

    def test_integrated_precedence(self):
        for test_str, val in test_strings_prec.items():
            self.assertEqual(val, evaluate_rpn(shunting_yard(test_str, operator_precedence)))
