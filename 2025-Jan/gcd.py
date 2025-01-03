import math

def read_file_and_process_gcd(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    max_gcd = 0
    best_group = []

    current_group = []
    for line in lines:
        line = line.strip()
        if line == "BREAK":
            if current_group:
                # Compute the GCD of the current group
                group_gcd = math.gcd(*[int(num) for num in current_group])
                if group_gcd > max_gcd:
                    max_gcd = group_gcd
                    best_group = current_group[:]
                current_group = []
        else:
            current_group.append(line)

    # Handle the last group in case the file doesn't end with "BREAK"
    if current_group:
        group_gcd = math.gcd(*[int(num) for num in current_group])
        if group_gcd > max_gcd:
            max_gcd = group_gcd
            best_group = current_group[:]

    return max_gcd, best_group

def main():
    # Replace 'ans.txt' with the actual file path if needed
    filename = input("filename: ")
    max_gcd, best_group = read_file_and_process_gcd(filename)
    print("Group with the highest GCD:")
    for number in best_group:
        print(number)
    print(f"\nHighest GCD: {max_gcd}")

if __name__ == "__main__":
    main()

