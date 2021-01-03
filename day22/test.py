from unittest import TestCase
from collections import deque
from day22.solution import load_decks, play, crab_combat, winscore, serialize_configuration, recursive_crab_combat

with open('day22/test_input.txt') as f:
    test_lines = [line for line in f.readlines()]


class TestSolution(TestCase):
    def test_load_decks(self):
        player1, player2 = load_decks(test_lines)
        player1_expected = deque([9, 2, 6, 3, 1])
        player2_expected = deque([5, 8, 4, 7, 10])
        self.assertEqual(player1_expected, player1)
        self.assertEqual(player2_expected, player2)

    def test_play(self):
        player1 = deque([9, 2, 6, 3, 1])
        player2 = deque([5, 8, 4, 7, 10])
        play(player1, player2)
        player1_expected = deque([2, 6, 3, 1, 9, 5])
        player2_expected = deque([8, 4, 7, 10])
        self.assertEqual(player1_expected, player1)
        self.assertEqual(player2_expected, player2)

    def test_play_until_win(self):
        player1 = deque([9, 2, 6, 3, 1])
        player2 = deque([5, 8, 4, 7, 10])
        crab_combat(player1, player2)
        player1_expected = deque()
        player2_expected = deque([3, 2, 10, 6, 8, 5, 9, 4, 7, 1])
        self.assertEqual(player1_expected, player1)
        self.assertEqual(player2_expected, player2)

    def test_winscore(self):
        player2 = deque([3, 2, 10, 6, 8, 5, 9, 4, 7, 1])
        self.assertEqual(306, winscore(player2))

    def test_serialize_configuration(self):
        player1 = deque([9, 2, 6, 3, 1])
        player2 = deque([5, 8, 4, 7, 10])
        expected = '9,2,6,3,1;5,8,4,7,10'
        self.assertEqual(expected, serialize_configuration(player1, player2))

    def test_recursive_crab_combat_empty_deck(self):
        player1 = deque([9, 2, 6, 3, 1])
        player2 = deque()
        res, player1_res, player2_res = recursive_crab_combat(player1, player2)
        self.assertTrue(res)
        self.assertTupleEqual(tuple(player1), tuple(player1_res))
        self.assertTupleEqual(tuple(player2), tuple(player2_res))
        res, player2_res, player1_res = recursive_crab_combat(player2, player1)
        self.assertFalse(res)
        self.assertTupleEqual(tuple(player1), tuple(player1_res))
        self.assertTupleEqual(tuple(player2), tuple(player2_res))

    def test_recursive_crab_combat(self):
        player1 = deque([9, 2, 6, 3, 1])
        player2 = deque([5, 8, 4, 7, 10])
        player1_wins, player1_res, player2_res = recursive_crab_combat(player1, player2)
        self.assertFalse(player1_wins)
        self.assertListEqual([], list(player1_res))
        self.assertListEqual([7, 5, 6, 2, 4, 1, 10, 8, 9, 3], list(player2_res))

    def test_recursive_crab_combat2(self):
        player1 = deque([43, 19])
        player2 = deque([2, 29, 14])
        player1_wins, player1_res, player2_res = recursive_crab_combat(player1, player2)
