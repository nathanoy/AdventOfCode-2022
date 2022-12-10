from solution import part2


def main():
    fname = "text.input.txt"

    with open(fname, "w") as f:
        op_count = 0

        def addx(x):
            nonlocal op_count
            f.write(f"addx {x}\n")
            op_count += 2

        def noop():
            nonlocal op_count
            f.write("noop\n")
            op_count += 1

        # OPERATIONS:

        addx(-5)

        while op_count < 6 * 40:
            noop()
    part2(fname)


if __name__ == '__main__':
    main()
