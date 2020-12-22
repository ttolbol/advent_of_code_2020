from unittest import TestCase
from day16.solution import (extract_rule,
                            build_ruleset,
                            check_field,
                            validate_number,
                            isnum,
                            extract_tickets,
                            find_ticket_scanning_error_rate,
                            get_valid_tickets,
                            find_ticket_fields,
                            field_product)

with open('day16/test_input.txt') as f:
    test_lines = [line for line in f.readlines()]

test_rule = ('class', 1, 3, 5, 7)
test_ruleset = {
    'class': (1, 3, 5, 7),
    'row': (6, 11, 33, 44),
    'seat': (13, 40, 45, 50)
}
test_tickets = [[7, 1, 14], [7, 3, 47], [40, 4, 50], [55, 2, 20], [38, 6, 12]]
test_fields = ['row', 'class', 'seat']


class TestSolution(TestCase):
    def test_extract_rule(self):
        self.assertTupleEqual(test_rule, extract_rule(test_lines[0]))

    def test_build_ruleset(self):
        self.assertDictEqual(test_ruleset, build_ruleset(test_lines))

    def test_check_field_true(self):
        valid_numbers = (1, 2, 3, 5, 6, 7)
        for num in valid_numbers:
            self.assertTrue(check_field(num, test_rule[1:]))

    def test_check_field_false(self):
        invalid_numbers = (0, 4, 8)
        for num in invalid_numbers:
            self.assertFalse(check_field(num, test_rule[1:]))

    def test_validate_number_true(self):
        valid_numbers = (7, 3, 47, 40, 50, 2, 20, 38, 6)
        for num in valid_numbers:
            self.assertTrue(validate_number(num, test_ruleset))

    def test_validate_number_false(self):
        invalid_numbers = (4, 55, 12)
        for num in invalid_numbers:
            self.assertFalse(validate_number(num, test_ruleset))

    def test_isnum(self):
        self.assertTrue(isnum('123'))
        self.assertFalse(isnum('abc'))

    def test_extract_tickets(self):
        self.assertListEqual(test_tickets, extract_tickets(test_lines))

    def test_find_ticket_scanning_error_rate(self):
        self.assertEqual(71, find_ticket_scanning_error_rate(test_tickets, test_ruleset))

    def test_get_valid_tickets(self):
        valid_tickets = [[7, 1, 14], [7, 3, 47]]
        self.assertListEqual(valid_tickets, get_valid_tickets(test_tickets, test_ruleset))

    def test_find_ticket_fields(self):
        self.assertListEqual(test_fields, find_ticket_fields(test_tickets, test_ruleset))

    def test_field_product(self):
        test_fields_departure = ['departure row', 'class', 'departure seat']
        self.assertEqual(7*14, field_product(test_tickets[0], test_fields_departure))
