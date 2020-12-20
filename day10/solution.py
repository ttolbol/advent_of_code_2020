from collections import defaultdict


def load_numbers_sorted(in_str):
    return sorted(int(num) for num in in_str.splitlines())


def differences(seq):
    seq = [0] + seq + [seq[-1] + 3]
    return [n - seq[i - 1] for i, n in enumerate(seq) if i > 0]


def frequency(seq):
    freq = {}
    for n in seq:
        freq[n] = freq.get(n, 0) + 1
    return freq


def count_combinations(numbers):
    combinations = defaultdict(int)
    combinations[numbers[-1]] = 1

    for number in numbers[-2::-1]:  # iterate backwards and sum up number of paths
        combinations[number] = combinations[number+1] + combinations[number+2] + combinations[number+3]
    return combinations[1] + combinations[2] + combinations[3]


if __name__ == '__main__':
    with open('input.txt') as f:
        numbers = load_numbers_sorted(f.read())
    freq = frequency(differences(numbers))
    print(freq[1]*freq[3])
    print(count_combinations(numbers))
