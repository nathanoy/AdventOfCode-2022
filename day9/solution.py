import dataclasses
from itertools import pairwise

FILE = "./input.txt"


def parse_raw() -> str:
    with open(FILE, "r") as src:
        for line in src:
            direction, steps = line.strip().split(" ")
            yield direction, int(steps)


def part1():
    @dataclasses.dataclass
    class Cord:
        x: int
        y: int

        def __repr__(self):
            return f"({self.x},{self.y})"

    class Rope:
        def __init__(self):
            self.cords_tail = Cord(0, 0)
            self.cords_head = Cord(0, 0)

            self.max_y = 6
            self.max_x = 6

            self.visited = set()

        def move(self, direction):
            steps = 1  # move is called multiple times
            match direction:
                case "R":
                    self.cords_head.x += steps
                case "L":
                    self.cords_head.x -= steps
                case "U":
                    self.cords_head.y += steps
                case "D":
                    self.cords_head.y -= steps
                case _:
                    assert False, f"{direction!r} as direction is invalid"

            self.follow()

            self.update_visited()

            self.update_max()
            assert not r.has_to_follow(), "Impossible"

        def update_visited(self):
            self.visited.add((self.cords_tail.x, self.cords_tail.y))

        def update_max(self):
            self.max_x = max(self.cords_head.x, self.max_x)
            self.max_y = max(self.cords_head.y, self.max_y)

        def follow(self):
            if not self.has_to_follow():
                return

            h, t = self.cords_head, self.cords_tail
            if h.x > t.x:
                t.x += 1
            if h.x < t.x:
                t.x -= 1
            if h.y > t.y:
                t.y += 1
            if h.y < t.y:
                t.y -= 1

        def has_to_follow(self):
            h, t = self.cords_head, self.cords_tail
            return not (((h.x - 1) <= t.x <= (h.x + 1)) and ((h.y - 1) <= t.y <= (h.y + 1)))

        def __repr__(self):
            return f"R(head={self.cords_head}, tail={self.cords_tail})"

        def print(self):
            for y in range(self.max_y - 1, -1, -1):
                for x in range(self.max_x):
                    if x == self.cords_head.x and y == self.cords_head.y:
                        print("H", end="")
                        continue
                    if x == self.cords_tail.x and y == self.cords_tail.y:
                        print("T", end="")
                        continue

                    print(".", end="")
                print()
            print()

    data = parse_raw()
    r = Rope()

    # r.print()
    for direction, steps in data:
        for _ in range(steps):
            r.move(direction)
            # print(r)
            # r.print()
    # print(r.visited)
    print(len(r.visited))


def part2():
    @dataclasses.dataclass
    class Cord:
        x: int
        y: int

        def __repr__(self):
            return f"({self.x},{self.y})"

    @dataclasses.dataclass
    class Tail:
        x: int
        y: int
        name: str

        def __repr__(self):
            return f"{self.name}({self.x},{self.y})"

    class Rope:
        def __init__(self, tail_len=9):
            # self.cords_tail = Cord(0, 0)
            # self.cords_head = Cord(0, 0)

            self.max_y = 6
            self.max_x = 6

            self.visited = set()

            self.tail = []
            for x in range(0, tail_len + 1):
                self.tail.append(Tail(0, 0, str(x)))

        @property
        def cords_head(self):
            return self.tail[0]

        def move(self, direction):
            steps = 1  # move is called multiple times
            match direction:
                case "R":
                    self.cords_head.x += steps
                case "L":
                    self.cords_head.x -= steps
                case "U":
                    self.cords_head.y += steps
                case "D":
                    self.cords_head.y -= steps
                case _:
                    assert False, f"{direction!r} as direction is invalid"

            self.follow()

            self.update_visited()

            self.update_max()
            # assert not r.has_to_follow(), "Impossible"

        def update_visited(self):
            self.visited.add((self.tail[-1].x, self.tail[-1].y))

        def update_max(self):
            self.max_x = max(self.cords_head.x + 4, self.max_x)
            self.max_y = max(self.cords_head.y + 4, self.max_y)

        def follow(self):
            for h, t in pairwise(self.tail):
                if not self.has_to_follow(h, t):
                    return

                if h.x > t.x:
                    t.x += 1
                if h.x < t.x:
                    t.x -= 1
                if h.y > t.y:
                    t.y += 1
                if h.y < t.y:
                    t.y -= 1

        def has_to_follow(self, h, t):
            # h, t = self.cords_head, self.cords_tail
            return not (((h.x - 1) <= t.x <= (h.x + 1)) and ((h.y - 1) <= t.y <= (h.y + 1)))

        def print(self):
            for y in range(self.max_y - 1, -self.max_y - 1, -1):
                for x in range(-self.max_x, self.max_x):
                    if x == self.cords_head.x and y == self.cords_head.y:
                        print("H", end="")
                        continue
                    for p in self.tail:

                        if x == p.x and y == p.y:
                            print(p.name, end="")
                            break
                    else:
                        print(".", end="")

                print()
            print()

    data = parse_raw()
    r = Rope()

    # r.print()
    for direction, steps in data:
        for _ in range(steps):
            r.move(direction)
            # print(r.tail)
            # print(r)
        # r.print()
    # print(r.visited)
    print(len(r.visited))


def solution():
    part1()
    part2()


if __name__ == '__main__':
    solution()
