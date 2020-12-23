from itertools import product
from collections import defaultdict


def get_neighbor_coords(coords, dim=3):
    return (tuple(coords[i] + diffs[i] for i in range(dim)) for diffs in product((-1, 0, 1), repeat=dim) if any(diffs))


def count_neighbors(cubes, dim=3):
    neighbors = defaultdict(int)
    for coords in cubes:
        for neighbor_coords in get_neighbor_coords(coords, dim=dim):
            neighbors[neighbor_coords] += 1
    return neighbors


def evolve(cubes, neighbor_counts):
    evolved = set()
    coordinates = set(neighbor_counts.keys())
    coordinates.update(cubes)
    for coords in coordinates:
        if coords in cubes and 2 <= neighbor_counts[coords] <= 3:   # if cube is active and has 2 or 3 neighbors
            evolved.add(coords)
        elif coords not in cubes and neighbor_counts[coords] == 3:  # if cube is inactive and has 3 neighbors
            evolved.add(coords)
    return evolved


def load_cubes(lines, dim=3):
    cubes = set()
    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            if char == '#':
                cubes.add((x, y, *(0,)*(dim-2)))
    return cubes


if __name__ == '__main__':
    with open('input.txt') as f:
        lines = [line for line in f.readlines()]

    # part 1
    cubes_3d = load_cubes(lines)
    for _ in range(6):
        cubes_3d = evolve(cubes_3d, count_neighbors(cubes_3d))
    print(len(cubes_3d))

    # part 2
    cubes_4d = load_cubes(lines, dim=4)
    for _ in range(6):
        cubes_4d = evolve(cubes_4d, count_neighbors(cubes_4d, dim=4))
    print(len(cubes_4d))

    # part 3
    cubes_4d = load_cubes(lines, dim=5)
    for _ in range(6):
        cubes_4d = evolve(cubes_4d, count_neighbors(cubes_4d, dim=5))
    print(len(cubes_4d))
