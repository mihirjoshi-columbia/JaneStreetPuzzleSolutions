import sys

def read_nine_digit_numbers(filename):
    valid_rows = []
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            row_str = line.strip()
            valid_rows.append(row_str)
    return valid_rows


def puzzle_matches_row(puzzle_row, candidate):
    for c in range(9):
        if puzzle_row[c] != -1:  # pre-filled
            if int(candidate[c]) != puzzle_row[c]:
                return False
    return True


def fill_puzzle_rows(puzzle, valid_rows):
    """
    Attempt to fill the 9x9 puzzle (list of 9 lists, each of length 9) row-by-row
    using only rows from 'valid_rows' (each a 9-digit string of digits).
    We do a backtracking approach, ensuring no column or box conflicts.
    """
    def is_valid_placement(row_idx, candidate):
        # Check if candidate row matches pre-filled numbers
        if not puzzle_matches_row(puzzle[row_idx], candidate):
            return False
            
        # Check column conflicts with previous rows
        for col in range(9):
            digit = int(candidate[col])
            for prev_row in range(row_idx):
                if puzzle[prev_row][col] == digit:
                    return False
                    
        # Check 3x3 box conflicts
        box_row = (row_idx // 3) * 3
        for col in range(9):
            digit = int(candidate[col])
            box_col = (col // 3) * 3
            for r in range(box_row, box_row + 3):
                if r >= row_idx:  # Don't check beyond current row
                    break
                for c in range(box_col, box_col + 3):
                    if puzzle[r][c] == digit:
                        return False
        return True

    def solve(row_idx):
        if row_idx == 9:  # Filled all rows successfully
            return True
            
        # Try each valid row as a candidate for current row
        for candidate in valid_rows:
            if is_valid_placement(row_idx, candidate):
                # Place the candidate row
                for col in range(9):
                    puzzle[row_idx][col] = int(candidate[col])
                    
                # Recursively try to fill remaining rows
                if solve(row_idx + 1):
                    return True
                    
                # If we get here, we need to backtrack
                for col in range(9):
                    puzzle[row_idx][col] = -1
                    
        return False

    return solve(0)


def print_puzzle(puzzle):
    """
    Print the puzzle in a nice 9x9 grid format.
    puzzle is a list of lists [ [r0c0, r0c1, ...], [r1c0, ...], ... ]
    with digits in 0..8 or -1 for empty.
    """
    for r in range(9):
        if r > 0 and r % 3 == 0:
            print("------+-------+------")
        row_str = []
        for c in range(9):
            if c > 0 and c % 3 == 0:
                row_str.append("|")
            val = puzzle[r][c]
            row_str.append(str(val) if val != -1 else ".")
        print(" ".join(row_str))
    print()


def main():
    # Read the 9-digit numbers from results.txt
    filename = input("filename: ")
    valid_rows = read_nine_digit_numbers(filename)

    # Example puzzle with digits [0..8], -1 for empty
    PUZZLE = [
        [-1, -1, -1,   -1, -1, -1,   -1, 2, -1],
        [-1, -1, -1,   -1, -1, -1,   -1, -1, 5],
        [-1, 2, -1,    -1, -1, -1,   -1, -1, -1],
        [-1, -1, 0,    -1, -1, -1,   -1, -1, -1],
        [-1, -1, -1,   -1, -1, -1,   -1, -1, -1],
        [-1, -1, -1,   2,  -1, -1,   -1, -1, -1],
        [-1, -1, -1,   -1, 0,  -1,   -1, -1, -1],
        [-1, -1, -1,   -1, -1, 2,    -1, -1, -1],
        [-1, -1, -1,   -1, -1, -1,   5,  -1, -1]
    ]

    print("Initial puzzle (digits 0..9, -1 means empty):")
    print_puzzle(PUZZLE)

    success = fill_puzzle_rows(PUZZLE, valid_rows)
    if success:
        print("Found a valid solution:")
        print_puzzle(PUZZLE)
    else:
        print("No valid solution found using those 9-digit rows.")


if __name__ == "__main__":
    sys.setrecursionlimit(10**7)
    main()

