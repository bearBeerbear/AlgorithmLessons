# Problem: Find maximum value of (sum of previous x values) - current y value
# Approach:
# 1. Read number of pairs
# 2. Read all pairs (x, y)
# 3. Sort pairs by (x + y) in ascending order
# 4. Initialize running sum s and answer variable
# 5. For each pair, calculate s - y and update answer if needed, then add x to running sum
# 6. Output the maximum value found

import sys


def main():
    # Read number of pairs
    n = int(sys.stdin.readline().strip())
    pairs = []

    # Read all pairs
    for _ in range(n):
        x, y = map(int, sys.stdin.readline().split())
        pairs.append((x, y))

    # Sort pairs by (x + y) in ascending order
    pairs.sort(key=lambda p: p[0] + p[1])

    # Initialize variables
    ans = -10 ** 18  # Very small number
    s = 0  # Running sum of x values

    # Iterate through sorted pairs
    for x, y in pairs:
        # Update answer with current (sum - y)
        ans = max(ans, s - y)
        # Add current x to running sum
        s += x

    # Output the result
    print(ans)


if __name__ == "__main__":
    main()