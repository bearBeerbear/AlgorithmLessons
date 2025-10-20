"""
Problem: Generate all permutations of numbers from 1 to n
Approach: Use Depth-First Search (DFS) with backtracking
- We maintain an array 'a' to store the current permutation
- We maintain a boolean array 'st' to track which numbers are already used
- At each position 'u', we try all numbers that haven't been used yet
- When we reach position 'n', we have a complete permutation and print it
- After trying a number, we backtrack by marking it as unused again
"""


def dfs(u):
    """
    DFS function to generate permutations recursively
    Args:
        u: Current position in the permutation we are filling
    """
    # Base case: when we've filled all n positions
    if u == n:
        # Print the complete permutation
        print(' '.join(map(str, a[:n])))
        return

    # Try all numbers from 1 to n at the current position
    for i in range(1, n + 1):
        # Check if number i is not used in current permutation
        if not st[i]:
            st[i] = True  # Mark number i as used
            a[u] = i  # Place number i at current position
            dfs(u + 1)  # Recursively fill next position
            st[i] = False  # Backtrack: mark number i as unused


if __name__ == "__main__":
    # Read input: the number n
    n = int(input())
    # Array to store the current permutation
    a = [0] * n
    # Boolean array to track used numbers (index 0 is unused, we use indices 1 to n)
    st = [False] * (n + 1)
    # Start DFS from position 0
    dfs(0)