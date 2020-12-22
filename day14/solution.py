def apply_mask(string, mask):
    masked_string = ''
    for val, mask in zip(string, mask):
        if mask == 'X':
            masked_string = masked_string + val
        else:
            masked_string = masked_string + mask
    return masked_string


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


if __name__ == '__main__':
    with open('input.txt') as f:
        instructions = [line for line in f.readlines()]

    cpu = CPU()

    for instruction in instructions:
        cpu.execute(instruction)
    print(cpu.memory_sum())