import re


def extract(in_str):
    lim_min, lim_max, char, password = re.search(r'(\d+)\-(\d+) (\w): (\w*)', in_str).groups()
    return lim_min, lim_max, char, password


def validate1(in_str):
    lim_min, lim_max, char, password = extract(in_str)
    return int(lim_min) <= len(re.findall(char, password)) <= int(lim_max)


def validate2(in_str):
    lim_min, lim_max, char, password = extract(in_str)
    return (password[int(lim_min)-1] == char) != (password[int(lim_max)-1] == char)


def part1(lines):
    return sum(validate1(line) for line in lines)


def part2(lines):
    return sum(validate2(line) for line in lines)


with open('input.txt') as f:
    lines = f.readlines()
    print(part1(lines))
    print(part2(lines))
