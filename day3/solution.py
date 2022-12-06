FILE_PATH = "./input.txt"


# a = "vJrwpWtwJgWrhcsFMMfFFhFp"
#
# l = len(a) // 2
# x, y = a[:l], a[l:]
# i = set(x).intersection(set(y))
# print(ord(i.pop()))
# print(ord("A") - 38)


def part1():
    items = []
    with open(FILE_PATH, "r") as src:
        for a in src:
            l = len(a) // 2
            x, y = a[:l], a[l:]
            le = set(x).intersection(set(y)).pop()
            if (le.islower()):
                x = ord(le) - 96
            else:
                x = ord(le) - 38
            items.append(x)
    print(sum(items))


def next_3(i):
    it = iter(i)
    while True:
        try:
            yield next(it), next(it), next(it)
        except StopIteration:
            return


def part2():
    items = []
    with open(FILE_PATH, "r") as src:
        for r1, r2, r3 in next_3(src):
            c = set(r1.strip()).intersection(set(r2.strip())).intersection(set(r3.strip())).pop()
            # c = set.intersection(set(r1.strip()), set(r2.strip()), set(r3.strip()), ).pop()
            le = c
            if (le.islower()):
                x = ord(le) - 96
            else:
                x = ord(le) - 38
            items.append(x)
    print(sum(items))


def solution():
    part1()
    part2()


if __name__ == '__main__':
    solution()
    print("Done")
