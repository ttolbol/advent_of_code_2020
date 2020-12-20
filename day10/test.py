from unittest import TestCase
from day10.solution import load_numbers_sorted, differences, frequency, count_combinations


class TestSolution(TestCase):
    test_str = '16\n10\n15\n5\n1\n11\n7\n19\n6\n12\n4'
    test_num = [1, 4, 5, 6, 7, 10, 11, 12, 15, 16, 19]

    def test_load_numbers_sorted(self):
        self.assertEqual(TestSolution.test_num, load_numbers_sorted(TestSolution.test_str))

    def test_differences(self):
        self.assertEqual([1, 3, 1, 1, 1, 3, 1, 1, 3, 1, 3, 3], differences(TestSolution.test_num))

    def test_frequency(self):
        self.assertEqual({1: 3, 2: 2, 3: 1}, frequency([1, 1, 2, 1, 3, 2]))

    def test_count_combinations(self):
        self.assertEqual(8, count_combinations(TestSolution.test_num))
