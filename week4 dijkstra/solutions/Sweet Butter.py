import heapq
import sys

"""
Dijkstra's Algorithm for Multiple Cow Pastures Problem

Problem: Find the optimal meeting point for cows from different pastures
such that the total travel distance for all cows is minimized.

Approach:
1. There are 'n' cows located at specific pastures, 'p' total pastures, and 'm' bidirectional paths
2. For each potential meeting point (pasture 1 to p), run Dijkstra to compute shortest paths
3. Calculate total distance all cows would travel to reach that meeting point
4. Find the meeting point with minimum total travel distance

Key points:
- Graph has bidirectional edges (add both directions)
- Multiple Dijkstra runs (one per potential meeting point)
- Sum distances from all cow locations for each meeting point
- Find minimum total distance

Complexity: O(P * (E log V)) where P is pastures, E is edges, V is vertices
"""

INF = 0x3f3f3f3f

class Graph:
    def __init__(self, max_nodes=810, max_edges=3010):
        self.n = 0
        self.p = 0
        self.m = 0
        self.cow = [0] * max_nodes  # Cow locations
        # Adjacency list arrays
        self.h = [-1] * max_nodes
        self.e = [0] * (2 * max_edges)  # *2 for bidirectional edges
        self.ne = [0] * (2 * max_edges)
        self.w = [0] * (2 * max_edges)
        self.idx = 0
        # Temporary arrays for Dijkstra
        self.dist = [INF] * max_nodes
        self.st = [False] * max_nodes

    def add_edge(self, a, b, c):
        """Add bidirectional edge between a and b with weight c"""
        # Add a->b
        self.e[self.idx] = b
        self.w[self.idx] = c
        self.ne[self.idx] = self.h[a]
        self.h[a] = self.idx
        self.idx += 1

        # Add b->a
        self.e[self.idx] = a
        self.w[self.idx] = c
        self.ne[self.idx] = self.h[b]
        self.h[b] = self.idx
        self.idx += 1

    def dijkstra(self, start):
        """Run Dijkstra from start node, return total distance from all cows to start"""
        # Reset distance and visited arrays
        self.dist = [INF] * len(self.dist)
        self.st = [False] * len(self.st)

        # Initialize priority queue
        heap = []
        self.dist[start] = 0
        heapq.heappush(heap, (0, start))

        while heap:
            current_dist, t = heapq.heappop(heap)

            if self.st[t]:
                continue
            self.st[t] = True

            # Update all neighbors
            i = self.h[t]
            while i != -1:
                j = self.e[i]
                if self.dist[j] > current_dist + self.w[i]:
                    self.dist[j] = current_dist + self.w[i]
                    heapq.heappush(heap, (self.dist[j], j))
                i = self.ne[i]

        # Calculate total distance for all cows to reach start point
        total_distance = 0
        for i in range(1, self.n + 1):
            cow_location = self.cow[i]
            if self.dist[cow_location] == INF:
                return INF  # Some cow cannot reach this meeting point
            total_distance += self.dist[cow_location]

        return total_distance

    def find_optimal_meeting_point(self):
        """Find the pasture that minimizes total travel distance for all cows"""
        min_total_distance = INF

        # Try each pasture as potential meeting point
        for meeting_point in range(1, self.p + 1):
            total_dist = self.dijkstra(meeting_point)
            if total_dist < min_total_distance:
                min_total_distance = total_dist

        return min_total_distance

def main():
    data = sys.stdin.read().split()
    if not data:
        return

    # Parse input: n cows, p pastures, m edges
    n = int(data[0])
    p = int(data[1])
    m = int(data[2])

    graph = Graph()
    graph.n = n
    graph.p = p
    graph.m = m

    # Read cow locations (index 1-based)
    idx = 3
    for i in range(1, n + 1):
        graph.cow[i] = int(data[idx])
        idx += 1

    # Read bidirectional edges
    for _ in range(m):
        a = int(data[idx])
        b = int(data[idx + 1])
        c = int(data[idx + 2])
        idx += 3
        graph.add_edge(a, b, c)

    # Find optimal meeting point
    result = graph.find_optimal_meeting_point()
    print(result)

if __name__ == "__main__":
    main()