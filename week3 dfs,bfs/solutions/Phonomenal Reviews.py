"""
Problem: Find the minimum total travel time to visit all pho restaurants in a tree structure.
Approach:
1. The problem reduces to finding the minimum path that covers all target nodes (pho restaurants) in a tree.
2. Key observation: The optimal path will traverse each edge in the minimal subtree that contains all pho restaurants at most twice.
3. We can reduce the problem by:
   - First building the tree from the given edges
   - Identifying the minimal subtree that contains all pho restaurants
   - The answer = 2 * (number of edges in minimal subtree) - longest path between two pho restaurants in this subtree
4. Steps:
   a. Mark which nodes are pho restaurants
   b. Use DFS to prune the tree, keeping only nodes that are pho restaurants or necessary for connectivity
   c. Find the diameter of the resulting subtree (longest path between any two pho restaurants)
   d. Calculate total time = 2 * (edges in minimal subtree) - diameter

Why this works:
- We need to visit all pho restaurants and return to start? Actually no return needed, so we can save the cost of returning from the farthest point.
- The formula: total_edges * 2 - diameter gives the minimum travel time where we start from one end of the diameter and finish at the other.
"""

import sys
sys.setrecursionlimit(300000)

def solve():
    # Read input
    n, m = map(int, sys.stdin.readline().split())
    pho_list = list(map(int, sys.stdin.readline().split()))

    # Mark pho restaurants
    is_pho = [False] * n
    for restaurant in pho_list:
        is_pho[restaurant] = True

    # Build adjacency list for the tree
    graph = [[] for _ in range(n)]
    for _ in range(n - 1):
        a, b = map(int, sys.stdin.readline().split())
        graph[a].append(b)
        graph[b].append(a)

    # First DFS: prune the tree to keep only necessary nodes
    # A node is necessary if it's a pho restaurant or connects pho restaurants
    necessary = [False] * n

    def mark_necessary(u, parent):
        # Mark node as necessary if it's a pho restaurant
        if is_pho[u]:
            necessary[u] = True
        # Check children
        for v in graph[u]:
            if v != parent:
                if mark_necessary(v, u):
                    necessary[u] = True
        return necessary[u]

    # Start from any pho restaurant
    start = pho_list[0]
    mark_necessary(start, -1)

    # Count edges in the minimal subtree
    edge_count = 0
    for i in range(n):
        if necessary[i]:
            for neighbor in graph[i]:
                if necessary[neighbor]:
                    edge_count += 1
    # Each edge counted twice, so divide by 2
    edge_count //= 2

    # Second DFS: find the diameter of the necessary subtree
    # First BFS/DFS to find the farthest node from start
    def find_farthest(start):
        dist = [-1] * n
        stack = [(start, -1, 0)]  # (node, parent, distance)
        farthest_node = start
        max_dist = 0

        while stack:
            u, parent, d = stack.pop()
            dist[u] = d
            if d > max_dist and necessary[u]:
                max_dist = d
                farthest_node = u
            for v in graph[u]:
                if v != parent and necessary[v]:
                    stack.append((v, u, d + 1))
        return farthest_node, max_dist

    # Find one end of diameter
    end1, _ = find_farthest(start)
    # Find the other end (farthest from end1) and get diameter length
    end2, diameter = find_farthest(end1)

    # Calculate result: 2 * edges - diameter
    result = 2 * edge_count - diameter
    print(result)

if __name__ == "__main__":
    solve()