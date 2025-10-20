"""
Problem: Generate All Combinations of Size m from Numbers 1 to n
Approach:
- We use depth-first search (DFS) with backtracking to generate all combinations
- Each combination is generated in lexicographical order by maintaining the 'start' parameter
- The 'start' parameter ensures we only consider numbers greater than the current one to avoid duplicates
- We build the combination one element at a time, storing in the 'way' array
- When we reach the required combination size (m), we print the current combination
Time Complexity: O(C(n, m) * m) where C(n, m) is the binomial coefficient
Space Complexity: O(m) for the recursion stack and the way array
"""


def dfs(u, start):
    """
    u: Current position in the combination we're building
    start: The smallest number we can choose for the current position
    """
    # Base case: when we've filled all m positions in the combination
    if u == m:
        # Print the current combination as space-separated numbers
        print(' '.join(map(str, way[:m])))
        return

    # Try all possible numbers from 'start' to n
    for i in range(start, n + 1):
        way[u] = i  # Choose number i for the current position
        # Recursively build the next position with numbers greater than i
        dfs(u + 1, i + 1)


if __name__ == "__main__":
    # Read input: n (range 1 to n) and m (combination size)
    n, m = map(int, input().split())
    # Initialize array to store the current combination being built
    way = [0] * m  # Only need m positions for the combination
    # Start DFS from position 0 with starting number 1
    dfs(0, 1)