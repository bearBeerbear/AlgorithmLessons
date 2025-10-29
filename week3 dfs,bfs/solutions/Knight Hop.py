from collections import deque


# Solution approach:
# This is a shortest path problem on an 8x8 chessboard where a knight moves in L-shapes.
# We can use BFS to find the minimum number of moves from start to target position.
# Knight moves: 8 possible L-shaped moves: (±1, ±2) and (±2, ±1)

def knight_shortest_path(start, target):
    # All possible knight moves (8 directions)
    moves = [
        (2, 1), (2, -1), (-2, 1), (-2, -1),
        (1, 2), (1, -2), (-1, 2), (-1, -2)
    ]

    # BFS initialization
    queue = deque()
    visited = [[False] * 9 for _ in range(9)]  # 1-indexed for convenience

    start_x, start_y = start
    target_x, target_y = target

    # Start position: distance 0
    queue.append((start_x, start_y, 0))
    visited[start_x][start_y] = True

    while queue:
        x, y, steps = queue.popleft()

        # Check if we reached the target
        if x == target_x and y == target_y:
            return steps

        # Try all possible knight moves
        for dx, dy in moves:
            new_x, new_y = x + dx, y + dy

            # Check if new position is valid and not visited
            if 1 <= new_x <= 8 and 1 <= new_y <= 8 and not visited[new_x][new_y]:
                visited[new_x][new_y] = True
                queue.append((new_x, new_y, steps + 1))

    return -1  # Should never happen for valid inputs


# Read input
start = tuple(map(int, input().split()))
target = tuple(map(int, input().split()))

# Calculate and output result
result = knight_shortest_path(start, target)
print(result)