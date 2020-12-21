from unittest import TestCase
from day11.solution import Seats, SeatsV2


class TestSolution(TestCase):
    test_str1 = ['L.LL.LL.LL',
                 'LLLLLLL.LL',
                 'L.L.L..L..',
                 'LLLL.LL.LL',
                 'L.LL.LL.LL',
                 'L.LLLLL.LL',
                 '..L.L.....',
                 'LLLLLLLLLL',
                 'L.LLLLLL.L',
                 'L.LLLLL.LL']

    test_str2 = ['#.##.##.##',
                 '#######.##',
                 '#.#.#..#..',
                 '####.##.##',
                 '#.##.##.##',
                 '#.#####.##',
                 '..#.#.....',
                 '##########',
                 '#.######.#',
                 '#.#####.##']

    test_str3 = ['#.LL.L#.##',
                 '#LLLLLL.L#',
                 'L.L.L..L..',
                 '#LLL.LL.L#',
                 '#.LL.LL.LL',
                 '#.LLLL#.##',
                 '..L.L.....',
                 '#LLLLLLLL#',
                 '#.LLLLLL.L',
                 '#.#LLLL.##']

    test_str4 = ['#.##.L#.##',
                 '#L###LL.L#',
                 'L.#.#..#..',
                 '#L##.##.L#',
                 '#.##.LL.LL',
                 '#.###L#.##',
                 '..#.#.....',
                 '#L######L#',
                 '#.LL###L.L',
                 '#.#L###.##']
    
    test_str5 = ['#.#L.L#.##',
                 '#LLL#LL.L#',
                 'L.#.L..#..',
                 '#L##.##.L#',
                 '#.#L.LL.LL',
                 '#.#L#L#.##',
                 '..L.L.....',
                 '#L#L##L#L#',
                 '#.LLLLLL.L',
                 '#.#L#L#.##']

    def test_count_adjacent(self):
        seats = Seats(TestSolution.test_str2)
        self.assertEqual(2, seats.count_adjacent(0, 0))
        self.assertEqual(5, seats.count_adjacent(2, 1))
        self.assertEqual(3, seats.count_adjacent(9, 5))

    def test_evolve(self):
        seats1 = Seats(TestSolution.test_str1)
        seats2 = Seats(TestSolution.test_str2)
        seats3 = Seats(TestSolution.test_str3)
        seats4 = Seats(TestSolution.test_str4)
        self.assertEqual(seats2, seats1.evolve())
        self.assertEqual(seats3, seats2.evolve())
        self.assertEqual(seats4, seats3.evolve())

    def test_final_form(self):
        seats1 = Seats(TestSolution.test_str1)
        seats5 = Seats(TestSolution.test_str5)
        self.assertEqual(seats5,  seats1.final_form())

    def test_count_occupied(self):
        seats5 = Seats(TestSolution.test_str5)
        self.assertEqual(37, seats5.count_occupied())

    def test_count_adjacent_v2(self):
        test_str = ['.......#.',
                     '...#.....',
                     '.#.......',
                     '.........',
                     '..#L....#',
                     '....#....',
                     '.........',
                     '#........',
                     '...#.....']
        seats = SeatsV2(test_str)
        self.assertEqual(8, seats.count_adjacent(3, 4))
        test_str = ['.............',
                    '.L.L.#.#.#.#.',
                    '.............']
        seats = SeatsV2(test_str)
        self.assertEqual(0, seats.count_adjacent(1, 1))
        
    def test_evolve_v2(self):
        test_str = ['#.LL.LL.L#',
                    '#LLLLLL.LL',
                    'L.L.L..L..',
                    'LLLL.LL.LL',
                    'L.LL.LL.LL',
                    'L.LLLLL.LL',
                    '..L.L.....',
                    'LLLLLLLLL#',
                    '#.LLLLLL.L',
                    '#.LLLLL.L#']
        seats2 = SeatsV2(TestSolution.test_str2)
        seats3 = SeatsV2(test_str)
        self.assertEqual(seats3, seats2.evolve())

    def test_final_form_v2(self):
        test_str = ['#.L#.L#.L#',
                    '#LLLLLL.LL',
                    'L.L.L..#..',
                    '##L#.#L.L#',
                    'L.L#.LL.L#',
                    '#.LLLL#.LL',
                    '..#.L.....',
                    'LLL###LLL#',
                    '#.LLLLL#.L',
                    '#.L#LL#.L#']
        seats1 = SeatsV2(TestSolution.test_str1)
        seats5 = SeatsV2(test_str)
        self.assertEqual(seats5,  seats1.final_form())
