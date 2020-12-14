def parse_instruction(in_str):
    instr, arg = in_str.split(' ')
    return instr, int(arg)


def execute_instruction(instr, arg, pc=0, acc=0):
    if instr == 'acc':
        acc += arg
        pc += 1
    elif instr == 'jmp':
        pc += arg
    else:
        pc += 1
    return pc, acc


def detect_loop(instructions):
    pc = 0
    acc = 0
    executed_instructions = set()
    while pc < len(instructions):
        if pc not in executed_instructions:
            executed_instructions.add(pc)
            pc, acc = execute_instruction(*instructions[pc], pc=pc, acc=acc)
        else:
            break
    return pc, acc, executed_instructions


def swap_instruction(instructions, i):
    instr, arg = instructions[i]
    if instr in ('nop', 'jmp'):
        if instr == 'nop':
            return 'jmp', arg
        else:
            return 'nop', arg
    return instructions[i]


def make_runnable(instructions):
    pc, acc, executed = detect_loop(instructions)
    if pc == len(instructions):  # original instruction set is already runnable, no changes needed!
        return acc
    for i in executed:
        swapped = swap_instruction(instructions, i)
        if swapped != instructions[i]:
            modified_instructions = [instr for instr in instructions]
            modified_instructions[i] = swapped
            pc, acc, _ = detect_loop(modified_instructions)
            if pc == len(instructions):
                return acc
    raise ValueError('Failed to make instruction set runnable')


if __name__ == '__main__':
    with open('input.txt') as f:
        data = f.read()
    instructions = [parse_instruction(part) for part in data.splitlines()]
    pc, acc, _ = detect_loop(instructions)
    print(acc)  # part 1
    print(make_runnable(instructions))



