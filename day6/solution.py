FILE_NAME = "./input.txt"

import json


def part1():
    with open(FILE_NAME, "r") as src:
        offsett = 0
        for line in src:
            line = line.rstrip("\n")
            for i in range(len(line)):
                if len(set(line[i:i + 4])) == 4:
                    print(i + 4)
                    break


def part2():
    with open(FILE_NAME, "r") as src:
        ofs = 14
        for line in src:
            line = line.rstrip("\n")
            for i in range(len(line)):
                if len(set(line[i:i + ofs])) == ofs:
                    print(i + ofs)
                    break


def solution():
    part1()
    part2()


if __name__ == '__main__':
    solution()
    print("\ndone!")
