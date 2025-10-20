"""
Problem: Sort an array using merge sort algorithm
Approach: Divide and conquer strategy
- Recursively split the array into two halves until we have single elements
- Merge the sorted halves back together in sorted order
- Time complexity: O(n log n) in all cases
- Space complexity: O(n) for temporary array
- Stable sorting algorithm (preserves relative order of equal elements)
"""


def merge_sort(q, l, r):
    """
    Recursive merge sort function
    Args:
        q: The array to be sorted
        l: Left index of the current subarray
        r: Right index of the current subarray
    """
    # Base case: subarray has 0 or 1 element (already sorted)
    if l >= r:
        return

    # Find the middle point to divide the array into two halves
    mid = (l + r) // 2

    # Recursively sort the left half
    merge_sort(q, l, mid)
    # Recursively sort the right half
    merge_sort(q, mid + 1, r)

    # Merge the two sorted halves
    k = 0  # Index for temporary array
    i = l  # Index for left subarray
    j = mid + 1  # Index for right subarray
    tmp = [0] * (r - l + 1)  # Temporary array to store merged result

    # Merge elements from both halves in sorted order
    while i <= mid and j <= r:
        if q[i] < q[j]:
            tmp[k] = q[i]  # Take element from left half
            i += 1
        else:
            tmp[k] = q[j]  # Take element from right half
            j += 1
        k += 1

    # Copy any remaining elements from left half
    while i <= mid:
        tmp[k] = q[i]
        i += 1
        k += 1

    # Copy any remaining elements from right half
    while j <= r:
        tmp[k] = q[j]
        j += 1
        k += 1

    # Copy the merged result from temporary array back to original array
    for i in range(l, r + 1):
        q[i] = tmp[i - l]


def main():
    """
    Main function to handle input and execute merge sort
    """
    # Read number of elements
    n = int(input())
    # Read the array to be sorted
    a = list(map(int, input().split()))
    # Sort the array using merge sort
    merge_sort(a, 0, n - 1)
    # Print the sorted array
    print(' '.join(map(str, a)))


if __name__ == "__main__":
    main()