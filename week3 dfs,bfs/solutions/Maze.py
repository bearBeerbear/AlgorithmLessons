"""
CCC 2008 S3: Maze
Solution Approach:
- Use DFS with backtracking to explore all possible paths from start (0,0) to end (row-1,col-1)
- Grid stores minimum steps to reach each cell, initialized to large value (99999)
- For each cell type:
  '+' : can move in all 4 directions
  '|' : can only move vertically (up/down)
  '-' : can only move horizontally (left/right)
  '*' : obstacle, cannot pass through
- Update grid only if current path has fewer steps than previous best
- Final answer is the value at bottom-right corner, or -1 if unreachable
"""

import sys

# Global variables for maze state
maze = []       # 2D array storing maze layout characters
grid = []       # 2D array storing minimum steps to reach each position
row = 0         # Number of rows in maze
col = 0         # Number of columns in maze

def traverse(r, c, x):
    """
    Recursive DFS function to explore maze paths
    Args:
        r: current row position
        c: current column position
        x: number of steps taken to reach current position
    """
    global maze, grid, row, col

    # Check if current position is within maze boundaries
    if r >= 0 and r < row and c >= 0 and c < col:
        # Check if current path is better than previous best and cell is not blocked
        if grid[r][c] >= 0 and x < grid[r][c]:

            # Obstacle cell - mark as unreachable
            if maze[r][c] == '*':
                grid[r][c] = -1

            # Crossroad - can move in all 4 directions
            elif maze[r][c] == '+':
                grid[r][c] = x  # Update with current step count
                # Recursively explore all four directions
                traverse(r - 1, c, x + 1)  # Move up
                traverse(r + 1, c, x + 1)  # Move down
                traverse(r, c - 1, x + 1)  # Move left
                traverse(r, c + 1, x + 1)  # Move right

            # Vertical path - can only move up/down
            elif maze[r][c] == '|':
                grid[r][c] = x
                # Only explore vertical directions
                traverse(r - 1, c, x + 1)  # Move up
                traverse(r + 1, c, x + 1)  # Move down

            # Horizontal path - can only move left/right
            elif maze[r][c] == '-':
                grid[r][c] = x
                # Only explore horizontal directions
                traverse(r, c - 1, x + 1)  # Move left
                traverse(r, c + 1, x + 1)  # Move right

def main():
    """
    Main function to handle input processing and output generation
    Reads multiple test cases from standard input
    """
    global maze, grid, row, col

    # Read all input data at once
    data = sys.stdin.read().splitlines()
    t = int(data[0])  # Number of test cases
    index = 1  # Current position in input data

    # Process each test case
    for k in range(t):
        # Read maze dimensions
        row = int(data[index]); index += 1
        col = int(data[index]); index += 1

        # Read maze layout
        maze = []
        for i in range(row):
            maze.append(list(data[index]))
            index += 1

        # Initialize grid with large values (unreachable by default)
        grid = [[99999] * col for _ in range(row)]

        # Start DFS traversal from top-left corner with 1 step
        traverse(0, 0, 1)

        # Output result for current test case
        # Check if bottom-right corner is reachable and has valid step count
        if grid[row - 1][col - 1] > 0 and grid[row - 1][col - 1] < 99999:
            print(grid[row - 1][col - 1])
        else:
            print(-1)

if __name__ == "__main__":
    main()