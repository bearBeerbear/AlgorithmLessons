# Problem: Parking lot management using union-find to find the next available parking space
# Approach:
# 1. Use union-find data structure where each parking space points to the next available space
# 2. When a car arrives wanting to park at space x, we find the next available space starting from x
# 3. If the found space is 0, it means no parking space is available
# 4. Otherwise, we assign the car to that space and update the parent to point to the next lower space
# 5. This efficiently finds the first available parking space in O(α(n)) time using path compression

def main():
    import sys

    # Read input
    data = sys.stdin.read().split()
    n = int(data[0])
    m = int(data[1])

    # Initialize parent array (1-indexed for parking spaces 1..n)
    parent = list(range(n + 1))

    def find(x):
        # Iterative find with path compression to avoid recursion depth issues
        stack = []
        current = x

        # Find the root
        while parent[current] != current:
            stack.append(current)
            current = parent[current]

        root = current

        # Path compression
        for node in stack:
            parent[node] = root

        return root

    # Process each car
    for i in range(m):
        x = int(data[2 + i])

        # Find the next available parking space starting from x
        available_space = find(x)

        if available_space == 0:
            # No parking space available
            print(i)
            return
        else:
            # Mark this space as occupied by pointing it to the next lower space
            parent[available_space] = available_space - 1

    # All cars parked successfully
    print(m)


if __name__ == "__main__":
    main()