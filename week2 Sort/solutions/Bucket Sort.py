"""
Bucket Sort for Finding K-th Smallest Element

Problem Analysis:
- We need to find the k-th smallest element in an array of n integers
- Instead of fully sorting the array, we can use bucket sort and stop when we find the k-th element
- This can be more efficient than full sorting when k is small

Algorithm Approach:
1. Distribute elements into buckets based on their value range
2. Sort buckets until we accumulate k elements
3. Stop early when we know we've reached the k-th smallest element
4. Return the k-th smallest element directly

Time Complexity: O(n + m) average case, where m is number of buckets processed
Space Complexity: O(n)
"""


def find_kth_smallest_bucket_sort(arr, k):
    """
    Find the k-th smallest element using bucket sort approach

    Args:
        arr: List of integers
        k: The k-th smallest element to find (1-indexed)

    Returns:
        The k-th smallest element in the array
    """
    if k < 1 or k > len(arr):
        raise ValueError("k must be between 1 and n")

    if len(arr) == 1:
        return arr[0]

    # Find range of values
    min_val = min(arr)
    max_val = max(arr)

    # If all elements are the same
    if min_val == max_val:
        return min_val

    # Calculate number of buckets (adjust based on input size)
    num_buckets = min(len(arr) // 5, 100)  # Reasonable limits
    num_buckets = max(num_buckets, 1)

    # Calculate bucket range
    bucket_range = (max_val - min_val + 1) / num_buckets

    # Create buckets
    buckets = [[] for _ in range(num_buckets)]

    # Distribute elements into buckets
    for num in arr:
        bucket_index = int((num - min_val) / bucket_range)
        bucket_index = min(bucket_index, num_buckets - 1)
        buckets[bucket_index].append(num)

    # Accumulate counts until we reach k-th element
    count = 0
    for i in range(num_buckets):
        # Sort current bucket
        buckets[i].sort()

        # If adding this bucket would exceed k
        if count + len(buckets[i]) >= k:
            # The k-th element is in this bucket
            return buckets[i][k - count - 1]
        else:
            # Add the count and continue
            count += len(buckets[i])

    # Should not reach here if k is valid
    raise ValueError("k is out of bounds")


def main():
    """
    Main function to handle input and output
    """
    # Read n and k
    n, k = map(int, input().strip().split())

    # Read the array of n integers
    arr = list(map(int, input().strip().split()))

    # Validate input
    if len(arr) != n:
        print(f"Error: Expected {n} numbers but got {len(arr)}")
        return

    if k > n or k < 1:
        print(f"Error: k must be between 1 and {n}")
        return

    # Find the k-th smallest element
    kth_smallest = find_kth_smallest_bucket_sort(arr, k)

    # Output the result
    print(kth_smallest)


# Execute the program
if __name__ == "__main__":
    main()