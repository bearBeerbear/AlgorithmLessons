"""
Problem: Determine if student p is taller than student q given M pairwise height comparisons.
Approach:
1. The comparisons form a directed graph where an edge x->y means x is taller than y.
2. If there exists a path from p to q, then p is taller than q.
3. If there exists a path from q to p, then p is shorter than q (q is taller than p).
4. If neither path exists, we cannot determine the relationship (unknown).

5. Since N and M can be up to 10^6 and 10^7 respectively, we need an efficient graph traversal.
6. We can use BFS or DFS to check connectivity from p to q and from q to p.

7. Steps:
   a. Build the graph from the given comparisons.
   b. Perform BFS/DFS from p to see if we can reach q.
   c. Perform BFS/DFS from q to see if we can reach p.
   d. Based on the results, output:
        - If p can reach q: "yes"
        - If q can reach p: "no"
        - Otherwise: "unknown"

8. Important: The graph could be large, so we need efficient data structures and algorithms.
"""

import sys
from collections import deque


def main():
    data = sys.stdin.read().split()
    if not data:
        print("unknown")
        return

    n = int(data[0])
    m = int(data[1])

    # Build adjacency list for the graph
    graph = [[] for _ in range(n + 1)]

    idx = 2
    for _ in range(m):
        x = int(data[idx])
        y = int(data[idx + 1])
        idx += 2
        graph[x].append(y)

    p = int(data[idx])
    q = int(data[idx + 1])

    # Function to check if there's a path from start to end using BFS
    def can_reach(start, end):
        if start == end:
            return True
        visited = [False] * (n + 1)
        queue = deque([start])
        visited[start] = True

        while queue:
            node = queue.popleft()
            for neighbor in graph[node]:
                if neighbor == end:
                    return True
                if not visited[neighbor]:
                    visited[neighbor] = True
                    queue.append(neighbor)
        return False

    # Check both directions
    if can_reach(p, q):
        print("yes")
    elif can_reach(q, p):
        print("no")
    else:
        print("unknown")


if __name__ == "__main__":
    main()