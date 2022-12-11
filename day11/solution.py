import dataclasses
import re
import typing

FILE = "./input.txt"


@dataclasses.dataclass
class Monkey:
    _id: int
    op: str
    test: int
    test_true: int
    test_false: int
    items: list[int]

    inspec_count: int = 0

    # PART2 speed improvement, exec_op() also worked in a reasonable amount of time
    op_val: int = 0
    op_fn: typing.Callable = None
    operator: str = ""

    def perform(self, val):
        return self.op_fn(val, self.op_val)


FN_S = [
    (lambda x, y: x * y),
    (lambda x, y: x * x),
    (lambda x, y: x + y),
    (lambda x, y: x + x),
]


def parse_raw(file_name=FILE):
    # print("Parsing")

    with open(file_name, "r") as src:
        content = src.read()

    for block in content.split("\n\n"):
        d = re.match(
            r"Monkey (?P<_id>\d+):[^:]*: (?P<items>[^\n]*)[^:]*: (?P<op>[^\n]*)[^:]*:[a-z ]*(?P<test>[^\n]*)[^:]*:[a-z ]*(?P<test_true>[^\n]*)[^:]*:[a-z ]*(?P<test_false>[^\n]*)",
            block).groupdict()
        for k in ("_id", "test", "test_true", "test_false"):
            d[k] = int(d[k])
        d["items"] = list(map(int, d["items"].split(',')))

        m = Monkey(**d)
        match = re.match(r"[^+\-*/]*(?P<op>.)\s(?P<num>\w+)", m.op).groupdict()
        try:
            match["num"] = int(match["num"])
        except ValueError:
            pass
        m.operator = match["op"]
        match match["op"], match["num"]:
            case "*", int(n):
                m.op_val = n
                m.op_fn = FN_S[0]
            case "*", str(n):
                m.op_fn = FN_S[1]
            case "+", int(n):
                m.op_val = n
                m.op_fn = FN_S[2]
            case "+", str(n):
                m.op_fn = FN_S[3]
            case _:
                assert False, "Invalid op"
        yield d["_id"], m


def exec_op(_op, v):
    d = {"old": v, }
    exec(_op, d)
    return d["new"]


def part1():
    data: dict[int, Monkey] = dict(parse_raw())
    # round
    for _ in range(20):
        for _id, monkey in data.items():
            for _ in range(len(monkey.items)):
                val = monkey.items.pop(0)
                val = exec_op(monkey.op, val)
                monkey.inspec_count += 1
                val = val // 3
                if (val % monkey.test) == 0:
                    data[monkey.test_true].items.append(val)
                else:
                    data[monkey.test_false].items.append(val)
    lst = [m.inspec_count for m in data.values()]
    lst.sort()
    max1, max2 = lst.pop(), lst.pop()
    print(max1 * max2)


def part2():
    data: dict[int, Monkey] = dict(parse_raw())
    const = 1
    for m in data.values():
        const *= m.test
    for round_num in range(10000):
        for _id, monkey in data.items():
            for _ in range(len(monkey.items)):
                val = monkey.items.pop(0)
                val = monkey.perform(val)
                # val = exec_op(monkey.op, val)
                monkey.inspec_count += 1

                val = val % const
                if (val % monkey.test) == 0:
                    data[monkey.test_true].items.append(val)
                else:
                    data[monkey.test_false].items.append(val)
    lst = [m.inspec_count for m in data.values()]
    # print(lst)
    lst.sort()
    max1, max2 = lst.pop(), lst.pop()
    print(max1 * max2)
    return data


def solution():
    part1()
    part2()


if __name__ == '__main__':
    solution()
