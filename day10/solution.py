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


if __name__ == '__main__':
    with open('input.txt') as f:
        numbers = load_numbers_sorted(f.read())
    freq = frequency(differences(numbers))
    print(freq[1]*freq[3])
