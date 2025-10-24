# Problem: Find the k-th smallest element in an array using quickselect
# Approach:
# 1. Read n (array size) and k (target position)
# 2. Read the array elements
# 3. Use quickselect (modified quicksort) to partially sort the array
# 4. Recursively partition the array until the k-th element is in its correct position
# 5. Output the k-th smallest element (0-indexed in array, so k-1)

def quick_sort(q, l, r):
    """
    Quick sort implementation that partitions array around pivot
    and recursively sorts left and right partitions
    """
    if l >= r:
        return

    # Initialize pointers and choose pivot (middle element)
    i = l - 1
    j = r + 1
    x = q[(i + j) // 2]  # Pivot element

    # Partition the array
    while i < j:
        # Move i right until finding element >= pivot
        i += 1
        while q[i] < x:
            i += 1

        # Move j left until finding element <= pivot
        j -= 1
        while q[j] > x:
            j -= 1

        # Swap elements if pointers haven't crossed
        if i < j:
            q[i], q[j] = q[j], q[i]

    # Recursively sort left and right partitions
    quick_sort(q, l, j)
    quick_sort(q, j + 1, r)


def main():
    # Read n and k
    n, k = map(int, input().split())

    # Read the array
    a = list(map(int, input().split()))

    # Sort the array using quick sort
    quick_sort(a, 0, n - 1)

    # Output the k-th smallest element (1-indexed in problem, 0-indexed in array)
    print(a[k - 1])


if __name__ == "__main__":
    main()