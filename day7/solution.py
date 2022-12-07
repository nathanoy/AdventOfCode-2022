import pprint

FILE = "input.txt"


def part1():
    filesystem = {}
    current = {}
    parentlist = []
    with open(FILE, "r") as src:

        for line in src:
            line = line.strip()
            if line.startswith("$"):
                # print("CMD:", line)
                if line.startswith("$ cd"):
                    _, cmd, name = line.split(" ")
                    # print(cmd, name)
                    if name == "..":
                        try:
                            # print(parentlist)
                            parentlist.pop()
                            current = parentlist[-1]
                        except IndexError:
                            current = filesystem.get("/", {})
                    else:

                        # print(current, current.get(name))
                        # pprint.pprint(filesystem)
                        current = current.get(name, {})
                        parentlist.append(current)
                        if name == "/":
                            filesystem[name] = current
            else:
                if line.startswith("dir"):
                    name = line.split(" ")[1]
                    # print("DIR:", name)
                    current[name] = current.get(name, {})
                else:
                    size, name = line.split(" ")
                    size = int(size)
                    # print("FILE:", size, name)
                    current[name] = size
            # print("FILESYSTEM", line)
            # pprint.pprint(filesystem)
            # pprint.pprint(current)
    # pprint.pprint(filesystem)

    sizes = []

    def size_of(cur):
        size = 0
        for k, v in cur.items():
            if isinstance(v, int):
                size += v
            else:
                s = size_of(v)
                print("SUBDIR", k, s)
                size += s
        sizes.append(size)
        return size

    so = size_of(filesystem)
    print("SIZEOF", so)

    x = sum(filter(lambda a: a <= 100000, sizes))
    print(x)


def part2():
    filesystem = {}
    current = {}
    parentlist = []
    with open(FILE, "r") as src:

        for line in src:
            line = line.strip()
            if line.startswith("$"):
                # print("CMD:", line)
                if line.startswith("$ cd"):
                    _, cmd, name = line.split(" ")
                    # print(cmd, name)
                    if name == "..":
                        try:
                            # print(parentlist)
                            parentlist.pop()
                            current = parentlist[-1]
                        except IndexError:
                            current = filesystem.get("/", {})
                    else:

                        # print(current, current.get(name))
                        # pprint.pprint(filesystem)
                        current = current.get(name, {})
                        parentlist.append(current)
                        if name == "/":
                            filesystem[name] = current
            else:
                if line.startswith("dir"):
                    name = line.split(" ")[1]
                    # print("DIR:", name)
                    current[name] = current.get(name, {})
                else:
                    size, name = line.split(" ")
                    size = int(size)
                    # print("FILE:", size, name)
                    current[name] = size
            # print("FILESYSTEM", line)
            # pprint.pprint(filesystem)
            # pprint.pprint(current)
    # pprint.pprint(filesystem)

    sizes = []

    def size_of(cur):
        size = 0
        for k, v in cur.items():
            if isinstance(v, int):
                size += v
            else:
                s = size_of(v)
                # print("SUBDIR", k, s)
                size += s
        sizes.append(size)
        return size

    so = size_of(filesystem)
    print("SIZEOF", so)
    # print(sizes)
    unused = 70000000 - max(sizes)
    print("UNUSED", unused)
    smalles = 70000000
    for x in sizes:
        if (unused + x) >= 30000000:
            # print(smalles, x)
            smalles = min(smalles, x)
    print(smalles)


def solution():
    part2()


if __name__ == '__main__':
    solution()
