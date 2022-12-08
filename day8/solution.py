FILE = "input.txt"


def part1():
    data_ = open(FILE, "r").read().strip()
    data = []
    vis_ma = []
    for line in data_.splitlines():
        x = list(line)
        data.append(list(map(int, list(line))))
        vis_ma.append([False] * len(x))

    for direction in range(4):
        vis_ma = list(map(list, zip(*vis_ma)))[::-1]
        # rotate it, algorithm works from top to bottom, when rotated all 4 sides considered
        data = list(map(list, zip(*data)))[::-1]

        for idx, row in enumerate(data):
            for i, cell in enumerate(row):
                m = -1  # m: maximum, if tree is higher => visible
                if idx > 0:  # first row is always visible
                    # check all trees above the current one, and remember the highest height: m
                    for x in data[:idx]:
                        m = max(x[i], m)
                        if m == 9: break  # just a little more performant, as no tree is higher than 9
                if m < cell:  # current tree visible, as all above smaller
                    vis_ma[idx][i] = True  # set the current one to visible

    print(sum(map(sum, vis_ma)))


def part2():
    data_ = open(FILE, "r").read().strip()
    data = []
    score_map = []
    for line in data_.splitlines():
        x = list(line)
        data.append(list(map(int, list(line))))
        score_map.append([0] * len(x))

    for i in range(len(data)):
        for j in range(len(data[0])):
            x = data[i][j]
            row = data[i]
            col = [a[j] for a in data]
            for rng in (col[:i][::-1], row[:j][::-1], col[i + 1:], row[j + 1:],):

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

    print(max(map(max, score_map)))


def solution():
    part1()
    part2()


if __name__ == '__main__':
    solution()
