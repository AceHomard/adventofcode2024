import pandas as pd

def check_safety(sublevels):
    diffs = [sublevels[i+1] - sublevels[i] for i in range(len(sublevels) - 1)]
    all_increasing = all(0 < diff <= 3 for diff in diffs)
    all_decreasing = all(-3 <= diff < 0 for diff in diffs)
    return all_increasing or all_decreasing

def is_safe(levels):
    if check_safety(levels):
        return True

    for i in range(len(levels)):
        sublevels = levels[:i] + levels[i+1:]
        if check_safety(sublevels):
            return True
    return False

def main():
    safe = 0
    with open("input.csv", "r") as file:
        for index, line in enumerate(file):
            levels = [float(x) for x in line.strip().split() if x]
            if is_safe(levels):
                print(f"{levels}: Safe")
                safe += 1
            else:
                print(f"{levels}: Unsafe")
        print(safe)

if __name__ == "__main__":
    main()
