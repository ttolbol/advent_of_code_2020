from math import prod

with open('input.txt') as f:
    data = [line.strip() for line in f.readlines()]


def count_trees(lines, slope, x=0, y=0, count=0):
    if y >= len(lines):
        return count
    line = lines[y]
    if line[x % len(line)] == '#':
        count += 1
    dx, dy = slope
    x += dx
    y += dy
    return count_trees(lines, slope, x, y, count)


# part 1
print(count_trees(data, (3, 1)))

# part 2
slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
print(prod([count_trees(data, slope) for slope in slopes]))
