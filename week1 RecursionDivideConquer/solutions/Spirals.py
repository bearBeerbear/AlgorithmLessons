"""
Problem: Print numbers in a spiral pattern starting from given number(s)

Approach:
1. Use DFS to fill a 100x100 grid with numbers in a clockwise spiral pattern
2. Start from the center (50,50) and move in directions: right, down, left, up
3. Change direction when encountering an empty cell in the next clockwise direction
4. After filling, find the bounding box of non-zero cells and print with proper formatting
"""

# Initialize a 100x100 grid with zeros
g = [[0] * 100 for _ in range(100)]

# Global direction variable: 0=right, 1=down, 2=left, 3=up
d = 3
# Direction vectors: right, down, left, up
dxy = [(1, 0), (0, 1), (-1, 0), (0, -1)]


def dfs(u, v, x, y):
    """
    Recursive function to fill grid with numbers in spiral pattern

    Args:
        u: current number to place
        v: target number to stop at
        x: current x position in grid
        y: current y position in grid
    """
    global d
    # Place current number at current position
    g[x][y] = u
    # Base case: reached target number
    if u == v:
        return

    # Calculate next direction (clockwise turn)
    nd = (d + 1) % 4
    # Check if cell in next direction is empty
    if g[x + dxy[nd][0]][y + dxy[nd][1]] == 0:
        d = nd  # Change direction if empty cell found

    # Recursive call to place next number
    dfs(u + 1, v, x + dxy[d][0], y + dxy[d][1])


def main():
    # Read input, support two formats
    data = input().split()
    if len(data) == 1:
        # Single number per line format
        x = int(data[0])
        y = int(input())
    else:
        # Two numbers in one line format
        x, y = map(int, data)

    # Start DFS from center of grid
    dfs(x, y, 50, 50)

    # Find bounding box of non-zero cells
    fi = fj = 100  # First row and column with non-zero
    li = lj = 0  # Last row and column with non-zero
    w = 0  # Maximum width needed for formatting

    # Calculate bounding box and maximum number width
    for i in range(100):
        for j in range(100):
            if g[i][j]:
                fi = min(fi, i)
                fj = min(fj, j)
                li = max(li, i)
                lj = max(lj, j)
                w = max(w, len(str(g[i][j])))

    # Print the grid within bounding box
    for i in range(fi, li + 1):
        for j in range(fj, lj + 1):
            if g[i][j]:
                # Right-align number with calculated width
                print(f"{g[i][j]:>{w}}", end="  ")
            else:
                # Print spaces for empty cells
                print(" " * w, end="  ")
        print()  # New line after each row


if __name__ == "__main__":
    main()