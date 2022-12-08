import pprint

FILE = "input.txt"


def part1():
    data_ = open(FILE, "r").read().strip()
    # print(repr(data))
    data = []
    vis_ma = []
    for line in data_.splitlines():
        x = list(line)
        data.append(list(map(int, list(line))))
        vis_ma.append([False] * len(x))
    # pprint.pprint(data)
    # pprint.pprint(vis_ma)
    for direction in range(4):
        vis_ma = list(map(list, zip(*vis_ma)))[::-1]
        data = list(map(list, zip(*data)))[::-1]
        for idx, row in enumerate(data, start=0):
            # print(row, data[:idx])
            for i, col in enumerate(row):
                m = -1
                if idx > 0:
                    for x in data[:idx]:
                        m = max(x[i], m)

                if m < col:
                    vis_ma[idx][i] = True

    # pprint.pprint(vis_ma)
    c = 0
    for x in vis_ma:
        c += sum(x)
    print(c)


def part2():
    data_ = open(FILE, "r").read().strip()
    # print(repr(data))
    data = []
    score_map = []
    for line in data_.splitlines():
        x = list(line)
        data.append(list(map(int, list(line))))
        score_map.append([0] * len(x))
    # pprint.pprint(data)
    # pprint.pprint(score_map)
    for i in range(len(data)):
        for j in range(len(data[0])):
            x = data[i][j]
            row = data[i]
            col = [a[j] for a in data]
            rngs = (col[:i][::-1], row[:j][::-1], col[i + 1:], row[j + 1:],)
            # print(i, j, x, rngs)

            for rng in rngs:

                if len(rng) == 0:
                    score_map[i][j] = 0
                    break
                d = 1
                for k in rng:
                    if k >= x:
                        break
                    d += 1
                d = min(d, len(rng))
                score_map[i][j] = d * max(score_map[i][j], 1)
                # print("   ", d, score_map[i][j], rng)

        #     print()
        #     break
        # break
        # s = 1
        # m = -1
        # for a in row[j + 1:]:
        #     print(a, m, x, a > x, m >= a)
        #     if a > x or m >= a:
        #         break
        #
        #     m = max(m, a)
        #     s *= a
        # if s == 1: s = 0
        # print(row, col, row[j + 1:], x, s)
        # score_map[i][j] = s

    # pprint.pprint(score_map)
    print(max(map(max, score_map)))


def solution():
    part1()
    part2()


if __name__ == '__main__':
    solution()
