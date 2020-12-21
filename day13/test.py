from unittest import TestCase
from day13.solution import argmin, departure_time, check_time, find_time


class TestSolution(TestCase):

    def test_argmin(self):
        vals = [10, 3, 17, 15]
        self.assertEqual(1, argmin(vals))

    def test_departure_time(self):
        self.assertEqual(944, departure_time(934, 59))

    def test_check_time(self):
        test_str = '7,13,x,x,59,x,31,19'
        buslist = test_str.split(',')
        busses = [(i, int(bus)) for i, bus in enumerate(buslist) if bus != 'x']
        self.assertTrue(check_time(1068781, busses))

    def test_find_time(self):
        test_str = '7,13,x,x,59,x,31,19'
        buslist = test_str.split(',')
        busses = [(i, int(bus)) for i, bus in enumerate(buslist) if bus != 'x']
        self.assertEqual(1068781, find_time(busses))
