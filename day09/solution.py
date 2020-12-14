import random


def load_numbers(in_str):
    return [int(num) for num in in_str.splitlines()]


def number_is_sum(preamble, num):
    preamble_set = set(preamble)
    for sum_x in preamble:
        sum_y = num - sum_x
        if sum_y in preamble_set:
            return True
    return False


def find_number_not_sum(sequence, preamble_len=5):
    for i in range(preamble_len, len(sequence)):
        preamble = sequence[i - preamble_len:i]
        num = sequence[i]
        if not number_is_sum(preamble, num):
            return num
    raise ValueError('Failed to find number')


def find_contiguous_sum_set(sequence, num):
    num_index = sequence.index(num)
    sums = [0 for _ in sequence[:num_index]]
    for i, n in enumerate(sequence[:num_index]):
        sums[i] = sums[i-1] + n
    for i_max, sum_max in enumerate(sums):
        for i_min, sum_min in enumerate(sums):
            if i_min >= i_max:
                break
            if sum_max - sum_min == num:
                return i_min + 1, i_max


if __name__ == '__main__':
    with open('input.txt') as f:
        numbers = load_numbers(f.read())
    num = find_number_not_sum(numbers, 25)
    print(num)
    i_min, i_max = find_contiguous_sum_set(numbers, num)
    sum_set = {n for n in numbers[i_min:i_max + 1]}
    print(min(sum_set) + max(sum_set))
