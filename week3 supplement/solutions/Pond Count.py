# Solution Approach:
# Count connected components of 'W' in an N×M grid (8-connectivity).
# Use iterative DFS with a stack to avoid recursion depth limit.
#
# Steps:
# 1. Read n, m and the grid (list of strings).
# 2. Initialize visited[][] as False.
# 3. For each cell (i,j):
#    - If g[i][j] == 'W' and not visited, start iterative DFS:
#      - Use a stack to store cells to visit.
#      - Mark current cell as visited, push to stack.
#      - While stack is not empty:
#        - Pop cell, explore all 8 neighbors.
#        - If neighbor is 'W', in bounds, not visited → mark and push.
#    - Each new DFS start → one pond.
# 4. Output the count.

n, m = map(int, input().split())
g = [input().strip() for _ in range(n)]  # Read n lines, each with m chars
visited = [[False] * m for _ in range(n)]

# 8 possible directions: up, down, left, right, and diagonals
directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]


def iterative_dfs(start_x, start_y):
    stack = [(start_x, start_y)]
    visited[start_x][start_y] = True

    while stack:
        x, y = stack.pop()  # Pop last element (DFS behavior)
        # Explore all 8 neighbors
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            # Check bounds, 'W', and not visited
            if 0 <= nx < n and 0 <= ny < m and g[nx][ny] == 'W' and not visited[nx][ny]:
                visited[nx][ny] = True
                stack.append((nx, ny))


cnt = 0
# Traverse all cells
for i in range(n):
    for j in range(m):
        if g[i][j] == 'W' and not visited[i][j]:
            iterative_dfs(i, j)
            cnt += 1  # New pond found

print(cnt)