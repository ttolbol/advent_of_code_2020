from math import cos, sin, radians


class Ship:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.direction = 0

    def execute(self, instruction):
        cmd, val = instruction[0], int(instruction[1:])
        if cmd == 'N':
            self.y += val
        elif cmd == 'S':
            self.y -= val
        elif cmd == 'E':
            self.x += val
        elif cmd == 'W':
            self.x -= val
        elif cmd == 'L':
            self.direction += val
        elif cmd == 'R':
            self.direction -= val
        elif cmd == 'F':
            self.x += int(round(cos(radians(self.direction)) * val))
            self.y += int(round(sin(radians(self.direction)) * val))


class Waypoint:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.wx = 10
        self.wy = 1

    def execute(self, instruction):
        cmd, val = instruction[0], int(instruction[1:])
        if cmd == 'N':
            self.wy += val
        elif cmd == 'S':
            self.wy -= val
        elif cmd == 'E':
            self.wx += val
        elif cmd == 'W':
            self.wx -= val
        elif cmd == 'L' or cmd == 'R':
            rad = radians(val)
            if cmd == 'R':
                rad = -rad
            wx = int(round(self.wx * cos(rad) - self.wy * sin(rad)))
            wy = int(round(self.wx * sin(rad) + self.wy * cos(rad)))
            self.wx = wx
            self.wy = wy
        elif cmd == 'F':
            self.x += self.wx * val
            self.y += self.wy * val


if __name__ == '__main__':
    with open('input.txt') as f:
        instructions = [line for line in f.readlines()]

    ship = Ship()
    for instr in instructions:
        ship.execute(instr)
    print(int(abs(ship.x) + abs(ship.y)))

    wp = Waypoint()
    for instr in instructions:
        wp.execute(instr)
    print(int(abs(wp.x) + abs(wp.y)))
