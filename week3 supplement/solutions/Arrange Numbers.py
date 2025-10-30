# This program generates all permutations of numbers 1 to n in reverse lexicographical order
# It uses DFS (Depth-First Search) with backtracking to generate permutations
# The algorithm builds permutations by selecting the largest available numbers first
# This ensures the output is in reverse lexicographical order

def dfs(u, n, st, ans):
    """
    DFS function to generate permutations

    Args:
        u: current depth/position in permutation
        n: total numbers to permute (1 to n)
        st: state array to track used numbers
        ans: array to store current permutation
    """
    if u == n:  # Base case: permutation complete
        print(' '.join(map(str, ans[:n])))  # Only print first n elements
        return

    # Try numbers from n down to 1 (reverse order)
    for i in range(n, 0, -1):
        if not st[i]:  # If number i is not used
            st[i] = True  # Mark as used
            ans[u] = i  # Place in current position
            dfs(u + 1, n, st, ans)  # Recurse to next position
            st[i] = False  # Backtrack: unmark for other permutations


def main():
    n = int(input().strip())
    # Use n+1 for 1-indexed arrays to avoid index issues
    st = [False] * (n + 1)  # State array to track used numbers (1-indexed)
    ans = [0] * n  # Array to store current permutation (size n)
    dfs(0, n, st, ans)


if __name__ == "__main__":
    main()