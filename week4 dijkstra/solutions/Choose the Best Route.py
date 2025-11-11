"""
Reverse Dijkstra from Destination to Multiple Sources

Problem: Find the shortest distance from multiple start nodes to a single destination.
The graph edges are given in reverse direction.

Approach:
1. The graph has edges stored in reverse direction (b -> a instead of a -> b)
2. Run Dijkstra once from the destination node s
3. Find the minimum distance from s to any of the k start nodes

Key insight:
- By reversing the edges and running Dijkstra from the destination,
  we effectively compute shortest paths from all nodes to the destination
- This is more efficient than running Dijkstra from each start node

Complexity: O((N + M) log N) per test case
"""

import heapq
import sys

INF = 0x3f3f3f3f

class Graph:
    def __init__(self, n):
        self.n = n
        self.graph = [[] for _ in range(n + 1)]

    def add_edge(self, a, b, c):
        # Note: edges are added in reverse direction (b -> a)
        self.graph[b].append((a, c))

    def dijkstra(self, start):
        """Run Dijkstra from start node and return distance array"""
        dist = [INF] * (self.n + 1)
        visited = [False] * (self.n + 1)
        dist[start] = 0

        heap = []
        heapq.heappush(heap, (0, start))

        while heap:
            current_dist, u = heapq.heappop(heap)

            if visited[u]:
                continue
            visited[u] = True

            for v, weight in self.graph[u]:
                new_dist = current_dist + weight
                if new_dist < dist[v]:
                    dist[v] = new_dist
                    heapq.heappush(heap, (new_dist, v))

        return dist

def main():
    data = sys.stdin.read().split()
    idx = 0

    results = []

    while idx < len(data):
        # Read n, m, s for each test case
        n = int(data[idx]); idx += 1
        m = int(data[idx]); idx += 1
        s = int(data[idx]); idx += 1  # destination node

        graph = Graph(n)

        # Read m edges (stored in reverse direction)
        for _ in range(m):
            a = int(data[idx]); idx += 1
            b = int(data[idx]); idx += 1
            c = int(data[idx]); idx += 1
            graph.add_edge(a, b, c)  # adds edge b->a with weight c

        # Read k start nodes
        k = int(data[idx]); idx += 1
        start_nodes = []
        for _ in range(k):
            start_nodes.append(int(data[idx])); idx += 1

        # Run Dijkstra from destination s
        dist = graph.dijkstra(s)

        # Find minimum distance to any start node
        min_dist = INF
        for node in start_nodes:
            if dist[node] < min_dist:
                min_dist = dist[node]

        if min_dist == INF:
            results.append("-1")
        else:
            results.append(str(min_dist))

    # Output all results
    print("\n".join(results))

if __name__ == "__main__":
    main()