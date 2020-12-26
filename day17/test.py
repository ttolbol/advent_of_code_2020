from unittest import TestCase
from day17.solution import get_neighbor_coords, load_cubes


with open('day17/test_input.txt') as f:
    test_lines = [line for line in f.readlines()]

test_cubes_3d = {(1, 0, 0), (2, 1, 0), (0, 2, 0), (1, 2, 0), (2, 2, 0)}
test_cubes_4d = {(1, 0, 0, 0), (2, 1, 0, 0), (0, 2, 0, 0), (1, 2, 0, 0), (2, 2, 0, 0)}


class TestSolution(TestCase):
    def test_load_cubes_3d(self):
        self.assertSetEqual(test_cubes_3d, load_cubes(test_lines, dim=3))

    def test_load_cubes_4d(self):

        self.assertSetEqual(test_cubes_4d, load_cubes(test_lines, dim=4))

    def test_get_neighbor_coords_3d(self):
        expected = {(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (1, 1, 0), (-1, 1, 0), (1, -1, 0), (-1, -1, 0),
                    (1, 0, 1), (-1, 0, 1), (0, 1, 1), (0, -1, 1), (1, 1, 1), (-1, 1, 1), (1, -1, 1), (-1, -1, 1),
                    (1, 0, -1), (-1, 0, -1), (0, 1, -1), (0, -1, -1), (1, 1, -1), (-1, 1, -1), (1, -1, -1),
                    (-1, -1, -1), (0, 0, 1), (0, 0, -1)}
        self.assertSetEqual(expected, set(get_neighbor_coords((0, 0, 0), dim=3)))

    def test_get_neighbor_coords_4d(self):
        expected = {(1, 0, 0, 0), (-1, 0, 0, 0), (0, 1, 0, 0), (0, -1, 0, 0), (1, 1, 0, 0), (-1, 1, 0, 0),
                    (1, -1, 0, 0), (-1, -1, 0, 0), (1, 0, 1, 0), (-1, 0, 1, 0), (0, 1, 1, 0), (0, -1, 1, 0),
                    (1, 1, 1, 0), (-1, 1, 1, 0),
                    (1, -1, 1, 0), (-1, -1, 1, 0), (1, 0, -1, 0), (-1, 0, -1, 0), (0, 1, -1, 0), (0, -1, -1, 0),
                    (1, 1, -1, 0), (-1, 1, -1, 0),
                    (1, -1, -1, 0), (-1, -1, -1, 0), (0, 0, 1, 0), (0, 0, -1, 0), (1, 0, 0, 1), (-1, 0, 0, 1),
                    (0, 1, 0, 1), (0, -1, 0, 1), (1, 1, 0, 1), (-1, 1, 0, 1),
                    (1, -1, 0, 1), (-1, -1, 0, 1), (1, 0, 1, 1), (-1, 0, 1, 1), (0, 1, 1, 1), (0, -1, 1, 1),
                    (1, 1, 1, 1), (-1, 1, 1, 1),
                    (1, -1, 1, 1), (-1, -1, 1, 1), (1, 0, -1, 1), (-1, 0, -1, 1), (0, 1, -1, 1), (0, -1, -1, 1),
                    (1, 1, -1, 1), (-1, 1, -1, 1),
                    (1, -1, -1, 1), (-1, -1, -1, 1), (0, 0, 1, 1), (0, 0, -1, 1), (1, 0, 0, -1), (-1, 0, 0, -1),
                    (0, 1, 0, -1), (0, -1, 0, -1), (1, 1, 0, -1), (-1, 1, 0, -1),
                    (1, -1, 0, -1), (-1, -1, 0, -1), (1, 0, 1, -1), (-1, 0, 1, -1), (0, 1, 1, -1), (0, -1, 1, -1),
                    (1, 1, 1, -1), (-1, 1, 1, -1),
                    (1, -1, 1, -1), (-1, -1, 1, -1), (1, 0, -1, -1), (-1, 0, -1, -1), (0, 1, -1, -1), (0, -1, -1, -1),
                    (1, 1, -1, -1), (-1, 1, -1, -1),
                    (1, -1, -1, -1), (-1, -1, -1, -1), (0, 0, 1, -1), (0, 0, -1, -1), (0, 0, 0, 1), (0, 0, 0, -1)}
        self.assertSetEqual(expected, set(get_neighbor_coords((0, 0, 0, 0), dim=4)))
