"""
Problem: Count the number of multisets containing only 4 and 5 that sum to N.
Approach:
1. We solve 4x + 5y = N for non-negative integers x, y.
2. Iterate over possible y (number of 5's) from 0 to N//5.
3. For each y, check if (N - 5*y) is non-negative and divisible by 4.
4. Count all valid y's.
"""


def main():
    N = int(input().strip())
    count = 0

    # y is the number of 5's
    for y in range(0, N // 5 + 1):
        remainder = N - 5 * y
        if remainder >= 0 and remainder % 4 == 0:
            count += 1

    print(count)


if __name__ == "__main__":
    main()