from pathlib import Path

INPUT_FILE = Path("./puzzle_input.txt")



def solve_part1():
    current_cal = 0
    current_index = 0
    max_cal = 0
    max_index = 0
    with open(INPUT_FILE, "r") as src:
        for line in src:
            if not line.strip():
                current_cal = 0
                current_index += 1
                continue
            cal = int(line)
            current_cal += cal
            if current_cal > max_cal:
                max_cal = current_cal
                max_index = current_index
    print(f"{max_cal = }\n{max_index = }")



def solve_part2():
    elves = list()
    current_cal = 0
    with open(INPUT_FILE, "r") as src:
        for line in src:
            if not line.strip():
                elves.append(current_cal)
                current_cal = 0
                continue
            cal = int(line)
            current_cal += cal

    elves.sort(reverse=True)
    top_3 = elves[:3]
    print(f"{sum(top_3) = }")

def solve():
    print("Solving part1")
    solve_part1()

    print("\nSolving part2")
    solve_part2()