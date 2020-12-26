from unittest import TestCase
from day19.solution import build_ruleset, build_pattern, get_rule, get_message, match_pattern


with open('day19/test_input.txt') as f:
    test_lines = [line for line in f.readlines()]

test_ruleset = {
    0: {(4, 1, 5)},
    1: {(2, 3), (3, 2)},
    2: {(4, 4), (5, 5)},
    3: {(4, 5), (5, 4)},
    4: 'a',
    5: 'b'
}

test_pattern = '(a((aa|bb)(ab|ba)|(ab|ba)(aa|bb))b)'


class TestSolution(TestCase):
    def test_get_rule(self):
        self.assertSetEqual({(4, 1, 5)}, get_rule('4 1 5'))
        self.assertSetEqual({(2, 3), (3, 2)}, get_rule('2 3 | 3 2'))
        self.assertEqual('a', get_rule('"a"'))

    def test_build_ruleset(self):
        self.assertDictEqual(test_ruleset, build_ruleset(test_lines))

    def test_build_regex(self):
        self.assertEqual(test_pattern, build_pattern(test_ruleset))

    def test_get_message(self):
        expected = ['ababbb', 'bababa', 'abbbab', 'aaabbb', 'aaaabbb']
        self.assertListEqual(expected, get_message(test_lines))

    def test_match_pattern(self):
        self.assertTrue(match_pattern(test_pattern, 'ababbb'))
        self.assertTrue(match_pattern(test_pattern, 'abbbab'))
        self.assertFalse(match_pattern(test_pattern, 'bababa'))
        self.assertFalse(match_pattern(test_pattern, 'aaabbb'))
        self.assertFalse(match_pattern(test_pattern, 'aaaabbb'))
