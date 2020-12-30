import re
from collections import defaultdict, deque
from itertools import product
from math import sqrt
from random import shuffle


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

    # def get_tile(self):
    #     if self.flipped_y:
    #         new_tile = [row for row in reversed(self.tile)]
    #     else:
    #         new_tile = [row for row in self.tile]
    #
    #     if self.flipped_x:
    #         for i, row in new_tile:
    #             new_tile[i] = ''.join(reversed(row))
    #
    #     # TODO rotate
    #     return new_tile


class TileMap:
    directions = ((0, 1), (1, 0), (0, -1), (-1, 0))

    def __init__(self, start_tile):
        self.n_tiles = 1
        self.tiles = {(0, 0): start_tile}
        self.free_coords = set(self.directions)

    def check_if_tile_fits(self, tile, coord):
        if coord not in self.free_coords:
            return False
        for edge_num, direction in enumerate(self.directions):
            x = coord[0] + direction[0]
            y = coord[1] + direction[1]
            if (x, y) in self.tiles:
                if tile.get_edge(edge_num) != self.tiles[(x, y)].get_edge(edge_num + 2):
                    return False
        return True

    def add_tile(self, tile, coord):
        self.tiles[coord] = tile
        self.free_coords.remove(coord)
        for direction in self.directions:
            x = coord[0] + direction[0]
            y = coord[1] + direction[1]
            if (x, y) not in self.tiles:
                self.free_coords.add((x, y))

    def get_start_coords(self):
        x = 0
        y = 0
        while (x - 1, y) in self.tiles:
            x -= 1
        while (x, y - 1) in self.tiles:
            y -= 1
        return x, y


def construct_tilemap(tiles):
    tile_id_queue = deque(tiles.keys())
    shuffle(tile_id_queue)
    tm = TileMap(tiles[tile_id_queue.popleft()])
    while tile_id_queue:
        print(f'Found {len(tm.tiles)} of {len(tiles)} tiles. ')
        success = False
        tile_id = tile_id_queue.popleft()
        tile = tiles[tile_id]
        for coord, rotation, fx, fy in product(tm.free_coords, range(4), (True, False), (True, False)):
            tile.rotation = rotation
            tile.flip_x = fx
            tile.flip_y = fy
            if tm.check_if_tile_fits(tile, coord):
                tm.add_tile(tile, coord)
                success = True
                break
        if not success:
            tile_id_queue.append(tile_id)
    print(f'Found {len(tm.tiles)} of {len(tiles)} tiles. ')
    return tm


if __name__ == '__main__':
    with open('input.txt') as f:
        lines = [line for line in f.readlines()]

    # part 1
    tiles = load_tiles(lines)
    tm = construct_tilemap(tiles)
    x, y = tm.get_start_coords()
    w = int(sqrt(len(tiles.keys())))
    print(w)
    result = tm.tiles[(x, y)].id * tm.tiles[(x + w, y)].id * tm.tiles[(x, y + w)].id * tm.tiles[(x + w, y + w)].id
    print(result)

