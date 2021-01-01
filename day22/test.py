from unittest import TestCase
from collections import deque
from day22.solution import load_decks, play, play_until_win, winscore

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
        play_until_win(player1, player2)
        player1_expected = deque()
        player2_expected = deque([3, 2, 10, 6, 8, 5, 9, 4, 7, 1])
        self.assertEqual(player1_expected, player1)
        self.assertEqual(player2_expected, player2)

    def test_winscore(self):
        player2 = deque([3, 2, 10, 6, 8, 5, 9, 4, 7, 1])
        self.assertEqual(306, winscore(player2))
