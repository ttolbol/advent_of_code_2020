from unittest import TestCase
from day12.solution import Ship, Waypoint


class TestSolution(TestCase):
    test_str = ['F10', 'N3', 'F7', 'R90', 'F11']

    def test_ship_execute(self):
        ship_positions = ((10, 0),
                          (10, 3),
                          (17, 3),
                          (17, 3),
                          (17, -8))
        ship = Ship()
        for i, instr in enumerate(TestSolution.test_str):
            x, y = ship_positions[i]
            ship.execute(instr)
            self.assertEqual(x, ship.x)
            self.assertEqual(y, ship.y)

    def test_waypoint_execute(self):
        ship_positions = ((100, 10),
                          (100, 10),
                          (170, 38),
                          (170, 38),
                          (214, -72))
        wp_positions = ((10, 1),
                        (10, 4),
                        (10, 4),
                        (4, -10),
                        (4, -10))
        wp = Waypoint()
        for i, instr in enumerate(TestSolution.test_str):
            x, y = ship_positions[i]
            wx, wy = wp_positions[i]
            wp.execute(instr)
            self.assertEqual(x, wp.x)
            self.assertEqual(y, wp.y)
            self.assertEqual(wx, wp.wx)
            self.assertEqual(wy, wp.wy)

    def test_waypoint_execute2(self):
        test_str = ['R90', 'L90', 'R180', 'L180', 'R270', 'L270', 'R360', 'L360']
        wp_positions = ((1, -10),
                        (10, 1),
                        (-10, -1),
                        (10, 1),
                        (-1, 10),
                        (10, 1),
                        (10, 1),
                        (10, 1))
        wp = Waypoint()
        for i, instr in enumerate(test_str):
            wx, wy = wp_positions[i]
            wp.execute(instr)
            self.assertEqual(wx, wp.wx)
            self.assertEqual(wy, wp.wy)
