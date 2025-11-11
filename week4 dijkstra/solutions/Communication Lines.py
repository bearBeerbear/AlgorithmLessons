"""
Binary Search + Dijkstra with Edge Cost Transformation

Problem: Find the minimum maximum edge weight such that the path from 1 to n
has at most k edges that exceed this weight.

Approach:
1. Use binary search on the maximum allowed edge weight
2. For each candidate value mid, transform the graph:
   - Edges with weight <= mid cost 0
   - Edges with weight > mid cost 1
3. Run Dijkstra to find the minimum "cost" (number of edges > mid) from 1 to n
4. If this cost <= k, mid is feasible; search for smaller values
5. If no feasible value found, return -1

Complexity: O(log(max_w) * (M log N))
"""

import heapq
import sys

INF = 0x3f3f3f3f

class Graph:
    def __init__(self, n):
        self.n = n
        self.graph = [[] for _ in range(n + 1)]
        self.max_weight = 0

    def add_edge(self, a, b, c):
        self.graph[a].append((b, c))
        self.graph[b].append((a, c))  # undirected graph
        self.max_weight = max(self.max_weight, c)

    def dijkstra_with_threshold(self, threshold):
        """
        Run Dijkstra where edge cost is 1 if weight > threshold, else 0
        Returns the minimum number of edges > threshold from 1 to n
        """
        dist = [INF] * (self.n + 1)
        visited = [False] * (self.n + 1)
        dist[1] = 0

        heap = []
        heapq.heappush(heap, (0, 1))

        while heap:
            current_cost, u = heapq.heappop(heap)

            if visited[u]:
                continue
            visited[u] = True

            # Early termination if reached destination
            if u == self.n:
                break

            for v, weight in self.graph[u]:
                # Cost is 1 if edge weight exceeds threshold, else 0
                cost = 1 if weight > threshold else 0
                new_cost = current_cost + cost

                if new_cost < dist[v]:
                    dist[v] = new_cost
                    heapq.heappush(heap, (new_cost, v))

        return dist[self.n]

def main():
    data = sys.stdin.read().split()
    idx = 0

    n = int(data[idx]); idx += 1
    m = int(data[idx]); idx += 1
    k = int(data[idx]); idx += 1

    graph = Graph(n)

    # Read edges
    for _ in range(m):
        a = int(data[idx]); idx += 1
        b = int(data[idx]); idx += 1
        c = int(data[idx]); idx += 1
        graph.add_edge(a, b, c)

    # Binary search for the minimum maximum edge weight
    left, right = 0, graph.max_weight + 1
    answer = -1

    while left < right:
        mid = (left + right) // 2

        # Check if we can find a path with at most k edges > mid
        cost = graph.dijkstra_with_threshold(mid)

        if cost <= k:
            # mid is feasible, try smaller values
            answer = mid
            right = mid
        else:
            # mid is not feasible, try larger values
            left = mid + 1

    print(answer)

if __name__ == "__main__":
    main()