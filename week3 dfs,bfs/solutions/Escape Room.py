"""
Problem: Determine if we can travel from (1,1) to (M,N) in a grid where from a cell with value x,
         we can jump to any cell (a,b) such that a * b = x.

Approach:
1. The key observation: Instead of simulating all possible jumps from each cell (which could be too many),
   we can work backwards from the destination or use BFS/DFS with an optimization.

2. Important insight: For a cell (r, c) with value v, the possible jumps are to cells (a, b) where a*b = v.
   But note: a and b must be valid row and column indices (1 <= a <= M, 1 <= b <= N).

3. However, checking all factor pairs for each cell could be inefficient for large values (up to 10^6).
   Instead, we can think differently: For each cell (r, c), we can jump to cells whose row and column
   multiply to grid[r][c]. But we can reverse this: For a cell (i, j), which cells can jump to it?
   Answer: Cells (a, b) where a*b = grid[i][j] and 1 <= a <= M, 1 <= b <= N.

4. But this still requires factoring numbers. Another approach:
   - We can traverse the grid and for each cell (i, j), we know its value v = grid[i][j].
   - Then we can mark all cells (a, b) with a*b = v as reachable from (i, j) if (i, j) is reachable.
   However, this could be O(M*N*sqrt(v)) which might be too slow.

5. Better approach (used here):
   - We'll use BFS starting from (1,1).
   - To avoid checking all factor pairs for each cell, we precompute for each value v, the list of
     valid (a, b) pairs such that a*b = v, 1<=a<=M, 1<=b<=N.
   - But precomputing for all possible v (up to 10^6) is feasible and efficient.

6. Steps:
   a. Precompute for each number from 1 to 1,000,000, the list of factor pairs (a, b) where a <= M and b <= N.
   b. Use BFS starting from (1,1), marking visited cells.
   c. For each visited cell (i, j) with value v, get all precomputed factor pairs for v and mark those cells as reachable.
   d. If we reach (M, N), output "yes", else "no".

7. Optimization:
   - We only need to precompute factor pairs where both factors are within grid bounds.
   - Use a visited array to avoid revisiting cells.

Time Complexity: O(M*N + V*log(V)) where V is the maximum value (10^6).
Space Complexity: O(M*N + V)
"""

from collections import deque
import sys


def main():
    # Read input
    M = int(sys.stdin.readline())
    N = int(sys.stdin.readline())

    grid = []
    for _ in range(M):
        row = list(map(int, sys.stdin.readline().split()))
        grid.append(row)

    # Precompute factor pairs for numbers up to 1,000,000
    # But we only care about pairs where a <= M and b <= N
    max_val = 1000000
    factors = [[] for _ in range(max_val + 1)]

    # For each possible factor a (row), find all b (column) such that a*b <= max_val
    for a in range(1, M + 1):
        for b in range(1, N + 1):
            product = a * b
            if product <= max_val:
                factors[product].append((a - 1, b - 1))  # Convert to 0-based indexing

    # BFS setup
    visited = [[False] * N for _ in range(M)]
    queue = deque()

    # Start from (0,0) in 0-based indexing
    start_val = grid[0][0]
    visited[0][0] = True
    queue.append((0, 0))

    # BFS traversal
    while queue:
        r, c = queue.popleft()

        # If we reached destination
        if r == M - 1 and c == N - 1:
            print("yes")
            return

        # Get the value at current cell
        val = grid[r][c]

        # For all reachable cells from this value
        for nr, nc in factors[val]:
            # Check if the cell is within bounds and not visited
            if 0 <= nr < M and 0 <= nc < N and not visited[nr][nc]:
                visited[nr][nc] = True
                queue.append((nr, nc))

    # If we never reached destination
    print("no")


if __name__ == "__main__":
    main()