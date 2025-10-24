# Problem: Calculate the weighted sum of sorted array where each element a[i] is multiplied by (n-i-1)
# Approach:
# 1. Read the integer n and the list of integers
# 2. Sort the list in ascending order
# 3. For each element at index i, multiply it by (n-i-1) and accumulate the result
# 4. Output the final accumulated result

def main():
    # Read number of elements
    n = int(input().strip())

    # Read the list of integers
    a = list(map(int, input().split()))

    # Sort the array in ascending order
    a.sort()

    # Initialize result variable
    res = 0

    # Calculate weighted sum
    for i in range(n):
        res += a[i] * (n - i - 1)

    # Output the result
    print(res)


if __name__ == "__main__":
    main()