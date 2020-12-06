with open('input.txt') as f:
    data = [int(line) for line in f.readlines()]


def part1(data):
    for idx1, num1 in enumerate(data):
        for num2 in data[idx1+1:]:
            if num1 + num2 == 2020:
                return num1 * num2


def part2(data):
    for num1 in data:
        for num2 in data:
            for num3 in data:
                if num1 + num2 + num3 == 2020:
                    return num1 * num2 * num3


print(part1(data))
print(part2(data))
