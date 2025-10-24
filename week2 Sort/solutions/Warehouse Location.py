# Problem: Calculate the sum of absolute differences from median
# Approach:
# 1. Read the array and sort it
# 2. Compute prefix sums for efficient range sum calculations
# 3. Find the median index (middle element in sorted array)
# 4. Calculate total cost:
#    - For elements before median: (median * count) - sum_of_left_elements
#    - For elements after median: sum_of_right_elements - (median * count)
# 5. Output the total cost

import sys


def main():
    # Read number of elements
    n = int(sys.stdin.readline().strip())

    # Read the array (1-indexed to match C++ code)
    a = [0] + list(map(int, sys.stdin.readline().split()))

    # Sort the array (from index 1 to n)
    a[1:] = sorted(a[1:])

    # Compute prefix sums
    s = [0] * (n + 1)
    for i in range(1, n + 1):
        s[i] = a[i] + s[i - 1]

    # Find median index (middle element)
    t = (n + 1) // 2

    # Calculate total cost:
    # For elements after median: (sum from t+1 to n) - a[t] * (n - t)
    # For elements before median: a[t] * t - (sum from 1 to t)
    result = (s[n] - s[t]) - a[t] * (n - t) + a[t] * t - s[t]

    print(result)


if __name__ == "__main__":
    main()