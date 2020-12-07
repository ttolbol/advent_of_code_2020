from unittest import TestCase
from day06.solution import split_groups, get_answers_anyone, get_answers_everyone


class TestSolution(TestCase):
    test_str = 'abc\n\na\nb\nc\n\nab\nac\n\na\na\na\na\n\nb\n'
    test_groups = [['abc'], ['a', 'b', 'c'], ['ab', 'ac'], ['a', 'a', 'a', 'a'], ['b']]

    def test_split_groups(self):
        result = split_groups(TestSolution.test_str)
        self.assertEqual(TestSolution.test_groups, result)

    def test_get_answers_anyone(self):
        results = [get_answers_anyone(group) for group in TestSolution.test_groups]
        expected_results = [{'a', 'b', 'c'}, {'a', 'b', 'c'}, {'a', 'b', 'c'}, {'a'}, {'b'}]
        for res, exp in zip(results, expected_results):
            self.assertEqual(exp, res)

    def test_get_answers_everyone(self):
        results = [get_answers_everyone(group) for group in TestSolution.test_groups]
        expected_results = [{'a', 'b', 'c'}, set(), {'a'}, {'a'}, {'b'}]
        for res, exp in zip(results, expected_results):
            self.assertEqual(exp, res)
