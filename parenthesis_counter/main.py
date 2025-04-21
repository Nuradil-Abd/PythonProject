import math

def count_well_formed_parenthesis(n: int) -> int:
    if not 1 <= n <= 15:
        raise ValueError("n must be between 1 and 15 inclusive")
    return math.comb(2 * n, n) // (n + 1)