"""
Problem: Robot navigation in a grid with conveyors and cameras
Approach:
1. Mark danger zones from cameras: any empty cell visible by any camera is dangerous
2. BFS from start cell, treating conveyor moves as 0-cost transitions
3. For normal moves (cost 1), follow conveyor chains immediately to find final stopping position
4. Skip positions that lead to loops or dangerous empty cells
5. Output shortest path to each empty cell (except start)

Key points:
- Conveyor moves don't count as steps
- Robots on conveyors are invisible to cameras
- Camera vision passes through conveyors but not walls
- Conveyor loops make paths invalid
"""

from collections import deque
import sys


def main():
    # Read input
    input = sys.stdin.read().splitlines()
    N, M = map(int, input[0].split())
    grid = [list(line.strip()) for line in input[1:1 + N]]

    # Find start position and all cameras
    start = None
    cameras = []
    for i in range(N):
        for j in range(M):
            if grid[i][j] == 'S':
                start = (i, j)
            elif grid[i][j] == 'C':
                cameras.append((i, j))

    # Mark danger zones: empty cells visible by cameras
    danger = [[False] * M for _ in range(N)]
    dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # up, down, left, right

    for i, j in cameras:
        danger[i][j] = True  # camera cell itself is dangerous
        for dx, dy in dirs:
            ni, nj = i + dx, j + dy
            # Extend vision in this direction until hitting a wall
            while 0 <= ni < N and 0 <= nj < M and grid[ni][nj] != 'W':
                if grid[ni][nj] in ('.', 'S'):
                    danger[ni][nj] = True  # mark empty cells as dangerous
                ni, nj = ni + dx, nj + dy

    # BFS for shortest path
    INF = 10 ** 9
    dist = [[INF] * M for _ in range(N)]

    # If start is in danger zone, no movement is possible
    if not danger[start[0]][start[1]]:
        dist[start[0]][start[1]] = 0
        q = deque([start])

        while q:
            x, y = q.popleft()

            # Handle conveyor moves (0 cost) - process immediately
            if grid[x][y] in 'LRUD':
                dx, dy = 0, 0
                if grid[x][y] == 'L':
                    dy = -1
                elif grid[x][y] == 'R':
                    dy = 1
                elif grid[x][y] == 'U':
                    dx = -1
                elif grid[x][y] == 'D':
                    dx = 1

                nx, ny = x + dx, y + dy
                # Check if conveyor move is valid
                if 0 <= nx < N and 0 <= ny < M and grid[nx][ny] != 'W':
                    if dist[nx][ny] > dist[x][y]:
                        dist[nx][ny] = dist[x][y]
                        q.appendleft((nx, ny))  # 0-cost moves go to front
                continue

            # Normal moves (cost 1) in four directions
            for dx, dy in dirs:
                nx, ny = x + dx, y + dy
                if 0 <= nx < N and 0 <= ny < M and grid[nx][ny] != 'W':
                    # Follow conveyor chain to find final stopping position
                    tx, ty = nx, ny
                    visited_conv = set()  # track visited conveyors to detect loops

                    # Follow the conveyor chain
                    while grid[tx][ty] in 'LRUD':
                        if (tx, ty) in visited_conv:
                            # Loop detected - invalid path
                            tx, ty = -1, -1
                            break
                        visited_conv.add((tx, ty))

                        ddx, ddy = 0, 0
                        if grid[tx][ty] == 'L':
                            ddy = -1
                        elif grid[tx][ty] == 'R':
                            ddy = 1
                        elif grid[tx][ty] == 'U':
                            ddx = -1
                        elif grid[tx][ty] == 'D':
                            ddx = 1

                        ntx, nty = tx + ddx, ty + ddy
                        if 0 <= ntx < N and 0 <= nty < M and grid[ntx][nty] != 'W':
                            tx, ty = ntx, nty
                        else:
                            break  # hit wall, stop at current position

                    if tx == -1:
                        continue  # skip looped paths

                    # Valid if stopped at conveyor or safe empty cell
                    if grid[tx][ty] in 'LRUD' or not danger[tx][ty]:
                        if dist[tx][ty] > dist[x][y] + 1:
                            dist[tx][ty] = dist[x][y] + 1
                            q.append((tx, ty))

    # Output results for all empty cells except start
    for i in range(N):
        for j in range(M):
            if grid[i][j] == '.' and (i, j) != start:
                print(-1 if dist[i][j] == INF else dist[i][j])


if __name__ == "__main__":
    main()