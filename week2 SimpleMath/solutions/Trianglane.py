"""
Problem: Calculate tape length needed to outline black triangles in a two-row pattern.
Approach:
1. Each black triangle initially contributes 3 units of tape (all 3 sides).
2. Subtract 2 units for each adjacent black triangle pair in the same row (shared side).
3. Subtract 2 units for each vertically adjacent black triangle pair in odd columns
   (due to triangular arrangement where only odd columns have vertical adjacency).
4. Process all tiles in row-major order to count and adjust tape length.
"""


def main():
    import sys

    # Read all input data
    input = sys.stdin.read
    data = input().split()

    n = int(data[0])  # Number of columns
    ans = 0

    # Initialize the grid with 3 rows (0,1,2) and n+2 columns for safe boundary checking
    # We use 1-based indexing to match the C++ code
    a = [[0] * (n + 2) for _ in range(4)]

    # Read the tile colors into the grid
    idx = 1
    for i in range(1, 3):  # Rows 1 and 2
        for j in range(1, n + 1):  # Columns 1 to n
            a[i][j] = int(data[idx])
            idx += 1

    # Calculate tape length
    for i in range(1, 3):  # Process both rows
        for j in range(1, n + 1):  # Process all columns
            if a[i][j] == 1:  # If tile is black
                ans += 3  # Add 3 units for the triangle's perimeter

                # Check left neighbor in same row
                if a[i][j - 1] == 1:  # If left tile is also black
                    ans -= 2  # Subtract 2 for the shared edge

                # Check top neighbor (only for row 2) in odd columns
                if i == 2 and a[i - 1][j] == 1 and j % 2 == 1:
                    ans -= 2  # Subtract 2 for the shared vertical edge

    print(ans)


if __name__ == "__main__":
    main()