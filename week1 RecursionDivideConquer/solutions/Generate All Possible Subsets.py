"""
Problem: Generate all non-empty subsets of {1, 2, ..., n} in lexicographical order
Approach:
1. Use depth-first search (DFS) to generate all subsets
2. Start from each number from 1 to n as the first element
3. For each starting number, recursively add larger numbers to build increasing sequences
4. Print each valid subset as it's generated to maintain lexicographical order

Key observations:
- Each subset is an increasing sequence (to avoid duplicates like [1,2] and [2,1])
- Lexicographical order is achieved by:
  - Starting from smallest numbers first
  - Always adding larger numbers in recursive calls
  - Printing immediately when a subset is formed

Example for n=3:
  Output will be: [1], [1,2], [1,2,3], [1,3], [2], [2,3], [3]
"""


def dfs(u, path):
    """
    Recursive DFS function to generate subsets

    Args:
        u: The last number added to the path (used to ensure increasing order)
        path: Current subset being built
    """
    # Print the current path immediately to maintain lexicographical order
    # This ensures we print subsets as we build them, in the correct sequence
    if path:
        print(' '.join(map(str, path)))

    # Iterate through all numbers greater than the last number added
    # This ensures the subset remains in increasing order and avoids duplicates
    for i in range(u + 1, n + 1):
        path.append(i)  # Choose number i
        dfs(i, path)  # Recursively build larger subsets
        path.pop()  # Backtrack: remove i to try other possibilities


# Read input: the maximum number n
n = int(input())

# Print empty line as specified (represents the empty subset, which is lexicographically smallest)
print()

# Start DFS from each number from 1 to n
# This ensures we generate all subsets starting with each possible first element
for start in range(1, n + 1):
    # Start with a subset containing only the starting number
    dfs(start, [start])