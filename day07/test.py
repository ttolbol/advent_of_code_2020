from unittest import TestCase
from day07.solution import (extract_bag_color,
                            get_rule,
                            get_rules,
                            invert_rules,
                            get_possible_bag_colors_containing_bag)


class TestSolution(TestCase):
    test_str = 'light red bags contain 1 bright white bag, 2 muted yellow bags.\n' \
               'dark orange bags contain 3 bright white bags, 4 muted yellow bags.\n' \
               'bright white bags contain 1 shiny gold bag.\n' \
               'muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.\n' \
               'shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.\n' \
               'dark olive bags contain 3 faded blue bags, 4 dotted black bags.\n' \
               'vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.\n' \
               'faded blue bags contain no other bags.\n' \
               'dotted black bags contain no other bags.\n'
    test_rules = {
        'light red': {'bright white', 'muted yellow'},
        'dark orange': {'bright white', 'muted yellow'},
        'bright white': {'shiny gold'},
        'muted yellow': {'shiny gold', 'faded blue'},
        'shiny gold': {'dark olive', 'vibrant plum'},
        'dark olive': {'faded blue', 'dotted black'},
        'vibrant plum': {'faded blue', 'dotted black'},
        'faded blue': set(),
        'dotted black': set()
    }
    inverted_rules = {
        'bright white': {'light red', 'dark orange'},
        'muted yellow': {'light red', 'dark orange'},
        'shiny gold': {'bright white', 'muted yellow'},
        'faded blue': {'muted yellow', 'dark olive', 'vibrant plum'},
        'dark olive': {'shiny gold'},
        'vibrant plum': {'shiny gold'},
        'dotted black': {'dark olive', 'vibrant plum'},
    }

    def test_extract_bag_color(self):
        test_strs = ['1 dark olive bag', '2 vibrant plum bags.']
        test_res = ['dark olive', 'vibrant plum']
        for test_str, expected in zip(test_strs, test_res):
            result = extract_bag_color(test_str)
            self.assertEqual(expected, result)

    def test_get_rule_single(self):
        test_str = 'light red bags contain 1 bright white bag, 2 muted yellow bags.\n'
        test_rule = ('light red', {'bright white', 'muted yellow'})
        result = get_rule(test_str)
        self.assertEqual(test_rule, result)

    def test_get_rule_multi(self):
        lines = TestSolution.test_str.split('\n')
        for line in lines:
            if line:
                key, val = get_rule(line)
                self.assertSetEqual(TestSolution.test_rules[key], val)

    def test_get_rules(self):
        result = get_rules(TestSolution.test_str)
        self.assertDictEqual(TestSolution.test_rules, result)

    def test_invert_rules(self):
        result = invert_rules(TestSolution.test_rules)
        self.assertDictEqual(TestSolution.inverted_rules, result)

    def test_get_possible_bag_colors_containing_bag(self):
        result = get_possible_bag_colors_containing_bag(TestSolution.inverted_rules, 'shiny gold')
        expected = {'bright white', 'muted yellow', 'dark orange', 'light red'}
        self.assertSetEqual(expected, result)
