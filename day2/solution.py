INPUT_FILE = r"./input.txt"


def desisions(x, y):
    map = {
        "A": 1,  # rock
        "B": 2,  # paper
        "C": 3,  # scissors
    }
    o = map.get(x)
    map2 = {
        "X": (((o - 2) % 3) + 1),  # need to losse
        "Y": o,  # draw
        "Z": ((o % 3) + 1)  # win
    }
    m = map2.get(y)
    return o, m


def winner(a, b):
    if a == b:
        return -1

    if ((a % 3) + 1) == b:
        # a lost
        return b
    return a


def points(x, winner):
    map = {
        -1: 3,
        x: 6,
    }
    return x + map.get(winner, 0)


def decode(x):
    map = {
        "A": 1,  # rock
        "B": 2,  # paper
        "C": 3,  # scissors

        "X": 1,  # need to loose
        "Y": 2,
        "Z": 3,
    }
    return map.get(x)


def part1():
    moves = []
    with open(INPUT_FILE, "r") as src:
        for line in src:
            if striped := line.strip():
                opponent, _, me = striped.partition(" ")
                moves.append((decode(opponent), decode(me)))

    score = 0
    for a, b in moves:
        w = winner(a, b)
        score += points(b, w)

    print(score)


def part2():
    moves = []
    with open(INPUT_FILE, "r") as src:
        for line in src:
            if striped := line.strip():
                opponent, _, me = striped.partition(" ")
                moves.append(((opponent, me), desisions(opponent, me)))

    score = 0
    for (o, m), (a, b) in moves:
        w = winner(a, b)
        p = points(b, w)
        # print(f"{o=} {m=} : {a}:{b} = {w} {p}")
        score += p

    print(score)


def solve():
    part1()

    part2()
