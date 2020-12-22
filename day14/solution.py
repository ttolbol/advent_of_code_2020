from itertools import product


def apply_mask(string, mask):
    masked_string = ''
    for val, mask_char in zip(string, mask):
        if mask_char == 'X':
            masked_string = masked_string + val
        else:
            masked_string = masked_string + mask_char
    return masked_string


def apply_mask_floating(string, mask):
    masked_string = ''
    n_floating = 0
    for val, mask_char in zip(string, mask):
        if mask_char == 'X':
            masked_string = masked_string + '{}'
            n_floating += 1
        elif mask_char == '0':
            masked_string = masked_string + val
        else:
            masked_string = masked_string + '1'

    return [masked_string.format(*comb) for comb in product('01', repeat=n_floating)]


def int2bin(val):
    # convert an integer value to 36-bit binary
    return bin(val)[2:].rjust(36, '0')


class CPU:
    def __init__(self):
        self.mask = 'X'*36
        self.memory = {}

    def memory_sum(self):
        return sum(self.memory.values())

    def set_mask(self, new_mask):
        self.mask = new_mask

    def write(self, address, value):
        self.memory[address] = int(apply_mask(int2bin(value), self.mask), 2)

    def execute(self, instruction):
        cmd, val = instruction.split(' = ')
        if cmd[:3] == 'mem':
            val = int(val)
            addr = int(cmd[4:-1])
            self.write(addr, val)
        else:
            self.set_mask(val)


class CPUv2(CPU):
    def write(self, address, value):
        for address in apply_mask_floating(int2bin(address), self.mask):
            self.memory[int(address, 2)] = value


if __name__ == '__main__':
    with open('input.txt') as f:
        instructions = [line for line in f.readlines()]

    # part 1
    cpu = CPU()
    for instruction in instructions:
        cpu.execute(instruction)
    print(cpu.memory_sum())

    # part 2
    cpu = CPUv2()
    for instruction in instructions:
        cpu.execute(instruction)
    print(cpu.memory_sum())
