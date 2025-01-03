from itertools import permutations

def generate_numbers(digits):
    """
    Given a list of digits (e.g. [1, 2, 3]),
    print all permutations joined as numbers (e.g. 123, 132, 213, 231, 312, 321).
    """
    for perm in permutations(digits):
        # perm is a tuple of digits, e.g. (1, 2, 3)
        number_str = "".join(map(str, perm))
        print(number_str)

# Example usage:
digits_list = [0, 2, 1, 3, 5, 4, 6, 7, 8]
generate_numbers(digits_list)

