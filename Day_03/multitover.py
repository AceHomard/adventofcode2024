import re

def main():
    safe_total = 0
    # Regex pour capturer mul(X, Y) où X et Y sont des nombres de 1 à 3 chiffres
    pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
    
    with open("exemple.txt", "r") as file:
        for line in file:
            matches = re.findall(pattern, line)
            for match in matches:
                x, y = map(int, match)
                result = x * y
                safe_total += result
                print(f"Valid mul({x},{y}) = {result}")
    
    print(f"Total of all valid mul operations: {safe_total}")

if __name__ == "__main__":
    main()
