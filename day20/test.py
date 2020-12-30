from unittest import TestCase
from day20.solution import load_tiles, Tile, find_matched_edges, TileMap

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

    def test_get_edge_rotated(self):
        tile = Tile(2311, test_tile)
        tile.rotation = 1
        self.assertEqual(test_edges[3], tile.get_edge(0))
        tile.rotation = 3
        self.assertEqual(test_edges[1], tile.get_edge(0))
        tile.flip_x = True
        self.assertEqual(test_edges_flip_x[1], tile.get_edge(0))
        tile.flip_y = True
        self.assertEqual(test_edges_flip_xy[1], tile.get_edge(0))


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

    def test_find_matched_edges(self):
        tiles = load_tiles(test_lines)
        matched_edges = {
            1951: 2,
            2311: 3,
            3079: 2,
            2729: 3,
            1427: 4,
            2473: 3,
            2971: 2,
            1489: 3,
            1171: 2
        }
        for tile_id, edges in matched_edges.items():
            self.assertEqual(edges, sum(find_matched_edges(tiles[tile_id], tiles.values())))

    def test_tilemap(self):
        tiles = load_tiles(test_lines)
        tm = TileMap(tiles.values())
        for key, val in tm.tiles.items():
            print(f'{key}: {val.id}')
        result = tm.tiles[(0, 0)].id * tm.tiles[(0, 2)].id * tm.tiles[(2, 0)].id * tm.tiles[(2, 2)].id
        self.assertEqual(result, 20899048083289)
