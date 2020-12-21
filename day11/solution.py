class Seats:
    def __init__(self, lines):
        self.h = len(lines)
        self.w = len(lines[0])
        self.mat = tuple(tuple(char for char in line) for line in lines)

    def __eq__(self, other):
        if isinstance(other, Seats):
            if self.h != other.h or self.w != other.w:
                return False
            for y in range(self.h):
                for x in range(self.w):
                    if self.mat[y][x] != other.mat[y][x]:
                        return False
            return True
        return False

    def count_adjacent(self, x, y):
        directions = ((1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1))
        count = 0
        for dx, dy in directions:
            if 0 <= x + dx < self.w and 0 <= y + dy < self.h and self.mat[y + dy][x + dx] == '#':
                count += 1
        return count

    def evolve(self):
        new_mat = [[char for char in line] for line in self.mat]
        for y in range(self.h):
            for x in range(self.w):
                if self.mat[y][x] != '.':
                    count = self.count_adjacent(x, y)
                    if self.mat[y][x] == 'L' and count == 0:
                        new_mat[y][x] = '#'
                    elif self.mat[y][x] == '#' and count >= 4:
                        new_mat[y][x] = 'L'
        return Seats(new_mat)

    def final_form(self):
        parent = self
        evolved = self.evolve()
        while evolved != parent:
            # THIS ISN'T EVEN MY FINAL FORM!
            parent = evolved
            evolved = evolved.evolve()
        return evolved

    def __repr__(self):
        lines = (''.join(line) for line in self.mat)
        return '\n'.join(lines)

    def count_occupied(self):
        return sum(sum(char == '#' for char in line) for line in self.mat)


class SeatsV2(Seats):
    def count_adjacent(self, x, y):
        directions = ((-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1))
        count = 0
        for dx, dy in directions:
            ix = x + dx
            iy = y + dy
            while 0 <= ix < self.w and 0 <= iy < self.h:
                if self.mat[iy][ix] == '#':
                    count += 1
                    break
                elif self.mat[iy][ix] == 'L':
                    break
                ix += dx
                iy += dy
        return count

    def evolve(self):
        new_mat = [[char for char in line] for line in self.mat]
        for y in range(self.h):
            for x in range(self.w):
                if self.mat[y][x] != '.':
                    count = self.count_adjacent(x, y)
                    if self.mat[y][x] == 'L' and count == 0:
                        new_mat[y][x] = '#'
                    elif self.mat[y][x] == '#' and count >= 5:
                        new_mat[y][x] = 'L'
        return SeatsV2(new_mat)


if __name__ == '__main__':
    with open('input.txt') as f:
        lines = [line for line in f.readlines()]

    print(Seats(lines).final_form().count_occupied())
    print(SeatsV2(lines).final_form().count_occupied())
