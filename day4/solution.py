FILE_NAME = "input.txt"


def part1():
    def parse(x):
        a1, _, a2 = x.partition("-")
        return int(a1), int(a2)

    sum = 0
    with open(FILE_NAME, "r") as src:
        for line in src:
            p1, _, p2 = line.strip().partition(",")
            pp1, pp2 = parse(p1), parse(p2)

            if pp2[1] == pp1[1] or pp2[1] == pp1[1]:
                sum += 1
                continue

            if pp1[1] > pp2[1]:  # make the bigger one the right one pp2
                pp1, pp2 = pp2, pp1

            if pp2[0] <= pp1[0]:
                sum += 1

    print(sum)


def part2():
    def parse(x):
        a1, _, a2 = x.partition("-")
        return int(a1), int(a2)

    sum = 0
    with open(FILE_NAME, "r") as src:
        for line in src:
            p1, _, p2 = line.strip().partition(",")
            pp1, pp2 = parse(p1), parse(p2)
            if pp2[1] == pp1[1] or pp2[1] == pp1[1]:
                sum += 1
                continue

            if pp1[1] > pp2[1]:  # make the bigger on the right one pp2
                pp1, pp2 = pp2, pp1

            if pp2[0] <= pp1[1]:
                sum += 1

    print(sum)


def solution():
    part1()
    part2()


if __name__ == '__main__':
    solution()
