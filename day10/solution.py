FILE = "./input.txt"


def parse_raw(file_name=FILE):
    print("Parsing")

    def parse_line(_line):
        if _line.startswith("addx"):
            a, b = _line.split(" ")
            return a, int(b)

        return _line, None

    with open(file_name, "r") as src:
        for line in src:
            line = line.rstrip()
            if not line:
                continue
            yield parse_line(line)


def part1():
    _X = 1
    cycle = []
    for instruction, value in parse_raw():
        # print(instruction, value)
        match instruction:
            case "noop":
                cycle.append(_X)
            case "addx":
                cycle.append(_X)
                cycle.append(_X)
                _X += value
            case _:
                assert False, "WHAT?"

    stren = []
    for i, v in enumerate(cycle, start=1):

        if (i + 20) % 40 == 0:
            # print(f"{i}: x = {v}, {i * v}")
            stren.append(i * v)
    print(sum(stren))


def part2(filename):
    _X = 1
    cycle = []
    for instruction, value in parse_raw(filename):
        match instruction:
            case "noop":
                cycle.append(_X)
            case "addx":
                cycle.append(_X)
                cycle.append(_X)
                _X += value
            case _:
                assert False, "WHAT?"

    for i, v in enumerate(cycle, start=1):
        x = (i - 1) % 40  # x is the horizontal index

        print("███" if v in range(x - 1, x + 2) else " . ", end="")

        if i % 40 == 0:
            print()


def solution():
    part1()
    part2(FILE)


if __name__ == '__main__':
    solution()
