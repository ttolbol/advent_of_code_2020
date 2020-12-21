from unittest import TestCase
from day12.solution import Ship, Waypoint


class TestSolution(TestCase):
    test_str = ['F10', 'N3', 'F7', 'R90', 'F11']

    def test_ship_execute(self):
        ship = Ship()
        for instr in TestSolution.test_str:
            ship.execute(instr)
        self.assertTupleEqual((17, -8), (ship.x, ship.y))

    def test_waypoint_execute(self):
        wp = Waypoint()
        for instr in TestSolution.test_str:
            wp.execute(instr)
        self.assertTupleEqual((214, -72), (wp.x, wp.y))
