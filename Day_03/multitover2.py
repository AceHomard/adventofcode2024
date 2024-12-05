import re

def main():
    safe_total = 0
    pattern = r"mul\((\d{1,3}),(\d{1,3})\)|don't\(\)|do\(\)"
    do = True
    with open("exemple.txt", "r") as file:
        for line in file:
            matches = re.finditer(pattern, line)
            for match in matches:
                if match.group(1) and match.group(2):
                    if do:
                        x, y = int(match.group(1)), int(match.group(2))
                        result = x * y
                        safe_total += result
                        print(f"Valid mul({x},{y}) = {result}")
                    else:
                        print(f"Skipped mul({match.group(1)},{match.group(2)}) due to 'don't'")
                elif "don't()" in match.group(0):
                    do = False
                    print("Found 'don't()' - Disabling mul operations")
                elif "do()" in match.group(0):
                    do = True
                    print("Found 'do()' - Enabling mul operations")

    print(f"Total of all valid mul operations: {safe_total}")

if __name__ == "__main__":
    main()
