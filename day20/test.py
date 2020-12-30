from unittest import TestCase
from day20.solution import load_tiles, Tile, TileMap, construct_tilemap

with open('day20/test_input.txt') as f:
    test_lines = [line for line in f.readlines()]

test_tile = ('..##.#..#.',
             '##..#.....',
             '#...##..#.',
             '####.#...#',
             '##.##.###.',
             '##...#.###',
             '.#.#.#..##',
             '..#....#..',
             '###...#.#.',
             '..###..###')

test_edges = ('..##.#..#.',
              '...#.##..#',
              '..###..###',
              '.#####..#.')

test_edges_flip_x = ('.#..#.##..',
                     '.#####..#.',
                     '###..###..',
                     '...#.##..#')

test_edges_flip_y = ('..###..###',
                     '#..##.#...',
                     '..##.#..#.',
                     '.#..#####.')

test_edges_flip_xy = ('###..###..',
                      '.#..#####.',
                      '.#..#.##..',
                      '#..##.#...')


class TestSolution(TestCase):
    def test_load_tiles(self):
        tiles = load_tiles(test_lines)
        self.assertEqual(Tile(2311, test_tile), tiles[2311])

    def test_tile(self):
        tile = Tile(2311, test_tile)
        self.assertEqual(2311, tile.id)
        self.assertTupleEqual(test_tile, tile.tile)
        self.assertTupleEqual(test_edges, tile.edges)

    def test_get_edge(self):
        tile = Tile(2311, test_tile)
        for i, edge in enumerate(test_edges):
            self.assertEqual(edge, tile.get_edge(i))

        tile.flip_x = True
        for i, edge in enumerate(test_edges_flip_x):
            self.assertEqual(edge, tile.get_edge(i))

        tile.flip_y = True
        for i, edge in enumerate(test_edges_flip_xy):
            self.assertEqual(edge, tile.get_edge(i))

        tile.flip_x = False
        for i, edge in enumerate(test_edges_flip_y):
            self.assertEqual(edge, tile.get_edge(i))

        tile.flip_y = False
        tile.rotation = -1
        for i, edge in enumerate(test_edges[1:-2]):
            self.assertEqual(edge, tile.get_edge(i))

        tile.flip_x = True
        for i, edge in enumerate(test_edges_flip_x[1:-2]):
            self.assertEqual(edge, tile.get_edge(i))

        tile.flip_y = True
        for i, edge in enumerate(test_edges_flip_xy[1:-2]):
            self.assertEqual(edge, tile.get_edge(i))

        tile.flip_x = False
        for i, edge in enumerate(test_edges_flip_y[1:-2]):
            self.assertEqual(edge, tile.get_edge(i))

    def test_tilemap(self):
        tiles = load_tiles(test_lines)
        tm = construct_tilemap(tiles)
        x, y = tm.get_start_coords()
        result = tm.tiles[(x, y)].id * tm.tiles[(x + 2, y)].id * tm.tiles[(x, y + 2)].id * tm.tiles[(x + 2, y + 2)].id
        self.assertEqual(20899048083289, result)
