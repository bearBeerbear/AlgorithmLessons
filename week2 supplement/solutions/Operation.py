import heapq


# Problem: Process operations to store numbers and retrieve/remove smallest numbers
# Operations:
#   1: Store a number (followed by the number to store)
#   2: Retrieve and remove the smallest stored number
# Insight: Use a min-heap to efficiently maintain numbers and retrieve minimum
# Min-heap allows O(log n) insertion and O(log n) removal of minimum element

def main():
    # Read number of operations
    n = int(input().strip())

    # Initialize min-heap (using list with heapq operations)
    heap = []

    # Process each operation
    for _ in range(n):
        # Read the entire line and split by spaces
        data = input().strip().split()

        # First element is the operation type
        operation = int(data[0])

        if operation == 1:
            # Operation 1: Store a number
            # Second element is the number to be stored
            num = int(data[1])
            # Push number to min-heap
            heapq.heappush(heap, num)

        else:  # operation == 2
            # Operation 2: Retrieve and remove smallest number
            if len(heap) == 0:
                # If heap is empty, output "NONONO"
                print("NONONO")
            else:
                # Get the smallest number from min-heap
                smallest = heapq.heappop(heap)
                # Output the smallest number
                print(smallest)


if __name__ == "__main__":
    main()