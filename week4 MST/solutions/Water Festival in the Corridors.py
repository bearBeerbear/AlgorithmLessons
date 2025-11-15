import sys
sys.setrecursionlimit(30000)

def main():
    """
    Problem: Count number of paths from node 1 to node n in a DAG
    Approach:
    1. The graph is a DAG (Directed Acyclic Graph) since slides only go from smaller to larger numbered nodes
    2. Use dynamic programming with dp[i] = number of paths from node i to node n
    3. Initialize dp[n] = 1 (one path: stay at n)
    4. Process nodes in reverse order from n-1 down to 1
    5. For each node u, dp[u] = sum of dp[v] for all neighbors v that u can slide to
    6. Answer is dp[1] - number of paths from start node 1 to end node n
    Time Complexity: O(n + m) where n is nodes, m is edges
    Space Complexity: O(n + m)
    """

    # Read number of nodes
    n = int(sys.stdin.readline().strip())

    # Build adjacency list
    graph = [[] for _ in range(n + 1)]

    while True:
        line = sys.stdin.readline().strip()
        if not line:
            continue
        x, y = map(int, line.split())
        if x == 0 and y == 0:
            break
        graph[x].append(y)

    # dp[i]: number of paths from i to n
    dp = [0] * (n + 1)
    dp[n] = 1  # base case: one path from n to n

    # Process nodes in reverse order (n down to 1)
    # Because edges go from small to large, processing from n to 1 ensures dependencies are computed
    for u in range(n - 1, 0, -1):
        for v in graph[u]:
            dp[u] += dp[v]

    # Output number of paths from 1 to n
    print(dp[1])

if __name__ == "__main__":
    main()