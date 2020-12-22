from unittest import TestCase
from day14.solution import CPU, apply_mask, int2bin


class TestSolution(TestCase):
    test_str = 'mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X\nmem[8] = 11\nmem[7] = 101\nmem[8] = 0'

    def test_int2bin(self):
        self.assertEqual('000000000000000000000000000000001011', int2bin(11))
        self.assertEqual('000000000000000000000000000001001001', int2bin(73))

    def test_apply_mask(self):
        val = '000000000000000000000000000000001011'
        mask = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X'
        expected = '000000000000000000000000000001001001'
        self.assertEqual(expected, apply_mask(val, mask))

    def test_execute_mask(self):
        instr = 'mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X'
        cpu = CPU()
        cpu.execute(instr)
        self.assertEqual('XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X', cpu.mask)

    def test_execute_mem(self):
        instr = 'mem[8] = 11'
        cpu = CPU()
        cpu.execute(instr)
        self.assertDictEqual({8: 11}, cpu.memory)

    def test_execute_multiple(self):
        instructions = TestSolution.test_str.split('\n')
        cpu = CPU()
        for instruction in instructions:
            cpu.execute(instruction)
        self.assertDictEqual({8: 64, 7: 101}, cpu.memory)

    def test_memory_sum(self):
        cpu = CPU()
        cpu.memory = {8: 64, 7: 101}
        self.assertEqual(165, cpu.memory_sum())
