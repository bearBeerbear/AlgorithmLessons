"""
Problem: Count reachable cells from starting position '@' in a grid with obstacles.
Approach:
1. Read grid dimensions (m columns, n rows) and the grid itself
2. Find the starting position marked with '@'
3. Use DFS to traverse all connected cells in 4 directions
4. Avoid obstacles ('#') and already visited cells
5. Count all reachable cells during DFS traversal
"""


def main():
    # Direction vectors for 4-directional movement
    dx = [-1, 0, 1, 0]  # up, right, down, left
    dy = [0, 1, 0, -1]

    # Read grid dimensions
    m, n = map(int, input().split())

    # Read the grid
    grid = []
    for i in range(n):
        grid.append(input().strip())

    # Find starting position '@'
    start_x, start_y = -1, -1
    for i in range(n):
        for j in range(m):
            if grid[i][j] == '@':
                start_x, start_y = i, j
                break
        if start_x != -1:
            break

    # Initialize visited matrix
    visited = [[False] * m for _ in range(n)]

    def dfs(x, y):
        """Depth-first search to count reachable cells from (x, y)"""
        # Mark current cell as visited
        visited[x][y] = True
        # Start count with current cell
        count = 1

        # Explore all 4 neighboring cells
        for i in range(4):
            a = x + dx[i]  # new row position
            b = y + dy[i]  # new column position

            # Check if new position is within grid boundaries
            if a < 0 or a >= n or b < 0 or b >= m:
                continue
            # Skip obstacles and already visited cells
            if grid[a][b] == '#' or visited[a][b]:
                continue

            # Recursively count reachable cells from neighbor
            count += dfs(a, b)

        return count

    # Perform DFS from starting position and print result
    result = dfs(start_x, start_y)
    print(result)


if __name__ == "__main__":
    main()