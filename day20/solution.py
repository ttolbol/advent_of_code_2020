import re
from collections import defaultdict, deque
from itertools import product
from math import sqrt


def load_tiles(lines):
    tiles = defaultdict(list)
    regex = re.compile(r'Tile (\d{4}):')
    for line in lines:
        match = regex.match(line)
        if match:
            key = int(match.group(1))
        elif line.strip():
            tiles[key].append(line.strip())
    return {key: Tile(key, val) for key, val in tiles.items()}


class Tile:
    def __init__(self, tile_id, tile):
        self.id = tile_id
        self.tile = tuple(row for row in tile)
        self.rotation = 0
        self.flip_x = False
        self.flip_y = False
        self.edges = (self.tile[0],
                      ''.join(row[-1] for row in self.tile),
                      self.tile[-1],
                      ''.join(row[0] for row in self.tile))

    def get_edge(self, edge):
        edge_index = (edge - self.rotation) % 4
        if self.flip_x and edge_index % 2 == 1:  # flip right and left edge
            edge_index = (edge_index + 2) % 4
        elif self.flip_y and edge_index % 2 == 0:  # flip top and bottom edge
            edge_index = (edge_index + 2) % 4
        if (self.flip_x and edge_index % 2 == 0) or (self.flip_y and edge_index % 2 == 1):
            return self.edges[edge_index][::-1]
        return self.edges[edge_index]

    def __eq__(self, other):
        if not isinstance(other, Tile):
            return False
        if self.id != other.id:
            return False
        if self.tile != other.tile:
            return False
        if self.rotation != other.rotation:
            return False
        if self.flip_x != other.flip_x:
            return False
        if self.flip_y != other.flip_y:
            return False
        if self.edges != other.edges:
            return False
        return True


class TileMap:
    directions = ((0, 1), (1, 0), (0, -1), (-1, 0))

    def __init__(self, tiles):
        tile_edges = defaultdict(deque)
        for tile in tiles:
            tile_edges[sum(find_matched_edges(tile, tiles))].append(tile)

        corner_tiles = tile_edges[2]
        edge_tiles = tile_edges[3]
        center_tiles = tile_edges[4]
        start_tile = corner_tiles.popleft()
        border_tiles = corner_tiles + edge_tiles

        # rotate start tile to align with lower left corner
        while find_matched_edges(start_tile, tiles) != (True, True, False, False):
            start_tile.rotation = (start_tile.rotation + 1) % 4

        self.size = int(sqrt(len(tiles)))
        self.tiles = {(0, 0): start_tile}
        self.free_coords = {self.directions[0]}

        for tile_queue in (border_tiles, center_tiles):
            while tile_queue:
                tile = tile_queue.popleft()
                success = False
                for coord, rotation, fx, fy in product(self.free_coords, range(4), (True, False), (True, False)):
                    tile.rotation = rotation
                    tile.flip_x = fx
                    tile.flip_y = fy
                    if self.check_if_tile_fits(tile, coord):
                        self.add_tile(tile, coord)
                        success = True
                        break
                if not success and tile_queue:
                    tile_queue.append(tile)
                print(f'Found {len(self.tiles)} of {len(tiles)} tiles. {len(tile_queue)} left in queue')

    def check_if_tile_fits(self, tile, coord):
        if coord in self.tiles:
            return False
        for edge_num, direction in enumerate(self.directions):
            x = coord[0] + direction[0]
            y = coord[1] + direction[1]
            if (x, y) in self.tiles and tile.get_edge(edge_num) != self.tiles[(x, y)].get_edge(edge_num + 2):
                return False
        return True

    def add_tile(self, tile, coord):
        self.tiles[coord] = tile
        self.free_coords.remove(coord)
        for direction in self.directions:
            x = coord[0] + direction[0]
            y = coord[1] + direction[1]
            if 0 <= x < self.size and 0 <= y < self.size and (x, y) not in self.tiles:
                self.free_coords.add((x, y))


def find_matched_edges(tile, tiles):
    matched = defaultdict(bool)
    for tile_test in tiles:
        if tile.id == tile_test.id:
            continue
        tile_config = tile_test.rotation, tile_test.flip_x, tile_test.flip_y
        for direction, rotation, fx, fy in product(range(4), range(4), (True, False), (True, False)):
            tile_test.rotation = rotation
            tile_test.flip_x = fx
            tile_test.flip_y = fy
            if matched[direction]:
                continue
            if tile.get_edge(direction) == tile_test.get_edge(direction + 2):
                matched[direction] = True
                break
        tile_test.rotation, tile_test.flip_x, tile_test.flip_y = tile_config
    return tuple(matched[i] for i in range(4))


if __name__ == '__main__':
    with open('input.txt') as f:
        lines = [line for line in f.readlines()]

    # part 1
    tiles = load_tiles(lines)
    tm = TileMap(tiles.values())
    result = tm.tiles[(0, 0)].id
    result *= tm.tiles[(tm.size - 1, 0)].id
    result *= tm.tiles[(0, tm.size - 1)].id
    result *= tm.tiles[(tm.size - 1, tm.size - 1)].id
    print(result)

    # part 2

