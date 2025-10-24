"""
Insertion Sort Algorithm

Problem Analysis:
- We need to sort an array of n integers in ascending order using insertion sort
- Insertion sort works by building a sorted portion from left to right
- For each element, we insert it into the correct position in the sorted portion

Algorithm Approach:
1. Start from the second element (index 1) as the first element is trivially sorted
2. For each element, compare it with elements in the sorted portion (to its left)
3. Shift all larger elements one position to the right to make space
4. Insert the current element into its correct position
5. Repeat until all elements are processed

Time Complexity: O(n²) in worst case, O(n) in best case (already sorted)
Space Complexity: O(1) - in-place sorting
Stability: Stable (equal elements maintain relative order)
"""


def insertion_sort(arr):
    """
    Sorts an array using insertion sort algorithm

    Args:
        arr: List of integers to be sorted

    Returns:
        List of integers sorted in ascending order
    """
    n = len(arr)

    # Iterate through each element starting from the second one
    for i in range(1, n):
        # Current element to be inserted into sorted portion
        key = arr[i]

        # Start from the last element of sorted portion
        j = i - 1

        # Shift all elements greater than key to the right
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        # Insert key at the correct position
        arr[j + 1] = key

    return arr


def main():
    """
    Main function to handle input and output
    """
    # Read number of elements
    n = int(input().strip())

    # Read the array of n integers
    arr = list(map(int, input().strip().split()))

    # Sort the array using insertion sort
    sorted_arr = insertion_sort(arr)

    # Output the sorted array as space-separated values
    print(" ".join(map(str, sorted_arr)))


# Execute the program
if __name__ == "__main__":
    main()