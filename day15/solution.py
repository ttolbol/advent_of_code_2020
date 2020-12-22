from collections import defaultdict, deque


class MemoryGame:
    def __init__(self, starting_numbers):
        self.sequence = deque()
        self.index_map = defaultdict(deque)
        for num in starting_numbers:
            self.add_num(num)

    def add_num(self, num):
        self.sequence.append(num)
        self.index_map[num].append(len(self.sequence) - 1)
        if len(self.index_map[num]) > 2:
            self.index_map[num].popleft()

    def iterate(self):
        last_num = self.sequence[-1]
        if len(self.index_map[last_num]) < 2:
            new_number = 0
        else:
            new_number = self.index_map[last_num][-1] - self.index_map[last_num][-2]
        self.add_num(new_number)
        return new_number

    def find_ith_number(self, i):
        while len(self.sequence) < i:
            self.iterate()
        return self.sequence[i-1]


if __name__ == '__main__':
    numbers = [8, 0, 17, 4, 1, 12]
    mg = MemoryGame(numbers)
    print(mg.find_ith_number(2020))
    print(mg.find_ith_number(30000000))
