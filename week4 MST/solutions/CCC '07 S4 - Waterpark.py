import sys
sys.setrecursionlimit(30000)

def main():
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