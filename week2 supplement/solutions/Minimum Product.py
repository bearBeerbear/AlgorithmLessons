# Problem: Minimize the sum of i * a_i by rearranging the array
# Insight: To minimize the weighted sum where weights are indices (1 to n),
# assign larger values to smaller weights and smaller values to larger weights
# Solution: Sort the array in descending order and compute sum(i * a_i)

def main():
    # Read number of elements
    n = int(input().strip())

    # Read the array elements
    a = []
    for _ in range(n):
        a.append(int(input().strip()))

    # Sort the array in descending order
    # This ensures larger values get multiplied by smaller indices
    a.sort(reverse=True)

    # Calculate the minimized sum
    # For each element at position i (0-indexed), the weight is (i+1)
    ans = 0
    for i in range(n):
        ans += (i + 1) * a[i]

    # Output the result
    print(ans)


if __name__ == "__main__":
    main()