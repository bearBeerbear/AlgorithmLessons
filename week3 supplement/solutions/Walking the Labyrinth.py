from collections import deque


# This program solves the maze shortest path problem using BFS
# BFS is used because it finds the shortest path in unweighted grid
# The algorithm explores all possible moves from start position level by level
# It uses a queue to process positions in the order they are discovered
# Distance array tracks the minimum steps to reach each position

def main():
    # Read n and m
    n, m = map(int, input().split())

    # Read the grid (1-indexed for easier boundary checking)
    grid = [[0] * (m + 2) for _ in range(n + 2)]
    for i in range(1, n + 1):
        row = list(map(int, input().split()))
        for j in range(1, m + 1):
            grid[i][j] = row[j - 1]

    # Initialize distance array with -1 (unvisited)
    dist = [[-1] * (m + 2) for _ in range(n + 2)]

    # Directions: up, right, down, left
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    # BFS initialization
    queue = deque()
    queue.append((1, 1))
    dist[1][1] = 0  # Start position has distance 0

    # BFS traversal
    while queue:
        x, y = queue.popleft()

        # Try all four directions
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            # Check boundaries
            if nx < 1 or ny < 1 or nx > n or ny > m:
                continue

            # Check if the cell is passable and not visited
            if grid[nx][ny] == 0 and dist[nx][ny] == -1:
                dist[nx][ny] = dist[x][y] + 1
                queue.append((nx, ny))

    # Output the distance to the target position
    print(dist[n][m])


if __name__ == "__main__":
    main()