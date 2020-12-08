from unittest import TestCase
from day08.solution import parse_instruction, execute_instruction, detect_loop, swap_instruction, make_runnable


class TestSolution(TestCase):
    test_str = 'nop +0\nacc +1\njmp +4\nacc +3\njmp -3\nacc -99\nacc +1\njmp -4\nacc +6\n'
    test_instructions = [('nop', 0),
                         ('acc', 1),
                         ('jmp', 4),
                         ('acc', 3),
                         ('jmp', -3),
                         ('acc', -99),
                         ('acc', 1),
                         ('jmp', -4),
                         ('acc', 6)]

    def test_parse_instruction(self):
        for expected, instruction in zip(TestSolution.test_instructions, TestSolution.test_str.split('\n')):
            self.assertEqual(expected, parse_instruction(instruction))

    def test_execute_instruction(self):
        self.assertEqual((1, 0), execute_instruction('nop', 0))
        self.assertEqual((1, 0), execute_instruction('nop', 10))
        self.assertEqual((6, 8), execute_instruction('nop', -20, pc=5, acc=8))
        self.assertEqual((0, 0), execute_instruction('jmp', 0))
        self.assertEqual((1, 0), execute_instruction('jmp', 1))
        self.assertEqual((2, 3), execute_instruction('jmp', -4, pc=6, acc=3))
        self.assertEqual((1, 0), execute_instruction('acc', 0))
        self.assertEqual((3, 23), execute_instruction('acc', 20, pc=2, acc=3))
        self.assertEqual((3, -17), execute_instruction('acc', -20, pc=2, acc=3))

    def test_detect_loop(self):
        pc, acc = detect_loop(TestSolution.test_instructions)
        self.assertEqual(5, acc)

    def test_detect_loop(self):
        expected = (1, 5, {0, 1, 2, 3, 4, 6, 7})
        self.assertEqual(expected, detect_loop(TestSolution.test_instructions))

    def test_detect_loop_terminates(self):
        # make modified instruction set with no loop
        modified_instructions = [instr for instr in TestSolution.test_instructions]
        modified_instructions[7] = ('nop', -4)
        pc, _, _ = detect_loop(modified_instructions)
        self.assertEqual(9, pc)

    def test_swap_instruction(self):
        self.assertEqual(('jmp', 0), swap_instruction(TestSolution.test_instructions, 0))
        self.assertEqual(('acc', 1), swap_instruction(TestSolution.test_instructions, 1))
        self.assertEqual(('nop', 4), swap_instruction(TestSolution.test_instructions, 2))

    def test_make_runnable(self):
        acc = make_runnable(TestSolution.test_instructions)
        self.assertEqual(8, acc)
