from unittest import TestCase
from day09.solution import load_numbers, number_is_sum, find_number_not_sum, find_contiguous_sum_set


class TestSolution(TestCase):
    test_str = '35\n20\n15\n25\n47\n40\n62\n55\n65\n95\n102\n117\n150\n182\n127\n219\n299\n277\n309\n576\n'
    test_num = [35, 20, 15, 25, 47, 40, 62, 55, 65, 95, 102, 117, 150, 182, 127, 219, 299, 277, 309, 576]

    def test_load_numbers(self):
        self.assertEqual(TestSolution.test_num, load_numbers(TestSolution.test_str))

    def test_number_is_sum(self):
        preamble = TestSolution.test_num[:5]
        num = TestSolution.test_num[5]
        self.assertTrue(number_is_sum(preamble, num))
        preamble = TestSolution.test_num[9:14]
        num = TestSolution.test_num[14]
        self.assertFalse(number_is_sum(preamble, num))

    def test_find_number_not_sum(self):
        self.assertEqual(127, find_number_not_sum(TestSolution.test_num))

    def test_find_contiguous_sum_set(self):
        i_min, i_max = find_contiguous_sum_set(TestSolution.test_num, 127)
        self.assertTupleEqual((2, 5), (i_min, i_max))
