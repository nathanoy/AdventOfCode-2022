FILE_NAME = "./input.txt"
FILE_NAME1 = "./input_1.txt"


def chunks(lst, n):
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), n):
        yield lst[i:i + n]


def part1():
    stacks = dict()

    with open(FILE_NAME1, "r") as src:
        for line in src:
            for i, stack in enumerate(chunks(line.rstrip("\n"), 4), start=1):

                if stack[1] != " ":
                    if stacks.get(i) is None:
                        stacks[i] = []
                    stacks[i].append(stack[1])

    for k in stacks.keys():
        stacks[k] = list(reversed(stacks[k]))

    def move(a, b):
        stacks[b].append(stacks[a].pop())

    with open(FILE_NAME, "r") as src:
        for line in src:
            _, x, _, y, _, z = line.strip().split()
            x, y, z = list(map(int, (x, y, z)))
            for _ in range(x):
                move(y, z)
    print("".join(stacks[i].pop() for i in range(1, len(stacks) + 1)))


def part2():
    stacks = dict()

    with open(FILE_NAME1, "r") as src:
        for line in src:
            for i, stack in enumerate(chunks(line.rstrip("\n"), 4), start=1):

                if stack[1] != " ":
                    if stacks.get(i) is None:
                        stacks[i] = []
                    stacks[i].append(stack[1])

    for k in stacks.keys():
        stacks[k] = list(reversed(stacks[k]))

    def move(times, a, b):
        tmp = []
        for _ in range(times):
            tmp.append(stacks[a].pop())  # fastest to write, not cleanest
        for g in reversed(tmp):
            stacks[b].append(g)

    with open(FILE_NAME, "r") as src:
        for line in src:
            _, x, _, y, _, z = line.strip().split()
            x, y, z = list(map(int, (x, y, z)))
            move(x, y, z)
    print("".join(stacks[i][-1] for i in range(1, len(stacks) + 1)))


def solution():
    part1()
    part2()


if __name__ == '__main__':
    solution()
    print("\ndone")
