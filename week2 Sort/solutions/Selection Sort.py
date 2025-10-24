# Problem: Sort an array using selection sort algorithm
# Approach:
# 1. Read the array size and elements
# 2. Implement selection sort:
#    - For each position i from 0 to n-2:
#    - Find the minimum element in the remaining unsorted part (from i to n-1)
#    - Swap the minimum element with the element at position i
# 3. Output the sorted array

def main():
    # Read number of elements
    n = int(input().strip())

    # Read the array
    q = list(map(int, input().split()))

    # Selection sort implementation
    for i in range(n - 1):
        # Find index of minimum element in unsorted part
        min_index = i
        for j in range(i + 1, n):
            if q[min_index] > q[j]:
                min_index = j

        # Swap the found minimum element with the first element of unsorted part
        q[i], q[min_index] = q[min_index], q[i]

    # Output the sorted array
    print(' '.join(map(str, q)))


if __name__ == "__main__":
    main()