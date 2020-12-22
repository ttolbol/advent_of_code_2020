from unittest import TestCase
from day14.solution import CPU, CPUv2, apply_mask, apply_mask_floating, int2bin


class TestSolution(TestCase):
    test_str = 'mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X\nmem[8] = 11\nmem[7] = 101\nmem[8] = 0'
    test_str2 = 'mask = 000000000000000000000000000000X1001X\nmem[42] = 100\nmask = 00000000000000000000000000000000X0XX\nmem[26] = 1'

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

    def test_apply_mask_floating(self):
        val = '000000000000000000000000000000101010'
        mask = '000000000000000000000000000000X1001X'
        expected = {'000000000000000000000000000000011010',
                    '000000000000000000000000000000011011',
                    '000000000000000000000000000000111010',
                    '000000000000000000000000000000111011'}
        self.assertEqual(expected, set(apply_mask_floating(val, mask)))

    def test_execute_multiple_v2(self):
        instructions = TestSolution.test_str2.split('\n')
        cpu = CPUv2()
        for instruction in instructions:
            cpu.execute(instruction)
        self.assertDictEqual({16: 1, 17: 1, 18: 1, 19: 1, 24: 1, 25: 1, 26: 1, 27: 1, 58: 100, 59: 100}, cpu.memory)
