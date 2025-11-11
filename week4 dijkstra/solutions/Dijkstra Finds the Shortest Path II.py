import heapq
import sys

"""
Dijkstra's Algorithm Implementation for Shortest Path

Problem: Find the shortest path from node 1 to node n in a weighted graph.

Approach:
1. Use adjacency list representation with arrays (similar to C++ style)
2. Implement Dijkstra's algorithm using min-heap priority queue
3. Maintain distance array to store shortest distances from source node
4. Use boolean array to track visited/processed nodes
5. If target node n is unreachable, return -1

Key differences from previous implementation:
- Uses array-based adjacency list instead of list of lists
- Closer to the original Java/C++ implementation style
- More memory efficient for large graphs
"""

INF = 0x3f3f3f3f  # Infinity value matching the Java code

class Dijkstra:
    def __init__(self, max_nodes=100010):
        # Initialize arrays similar to Java version
        self.N = max_nodes
        self.h = [-1] * self.N  # Head pointers for adjacency lists
        self.e = [0] * self.N   # Edge destinations
        self.ne = [0] * self.N  # Next pointers
        self.w = [0] * self.N   # Edge weights
        self.idx = 0            # Current index for edge storage
        self.dist = [INF] * self.N  # Shortest distances from node 1
        self.st = [False] * self.N  # Visited nodes

    def add_edge(self, a, b, c):
        """Add directed edge from a to b with weight c"""
        self.e[self.idx] = b
        self.w[self.idx] = c
        self.ne[self.idx] = self.h[a]
        self.h[a] = self.idx
        self.idx += 1

    def dijkstra(self, n):
        """Find shortest path from node 1 to all nodes using Dijkstra's algorithm"""
        # Reset arrays for new computation
        self.dist = [INF] * self.N
        self.st = [False] * self.N

        # Min-heap: (distance, node)
        heap = []
        heapq.heappush(heap, (0, 1))
        self.dist[1] = 0

        while heap:
            # Get node with smallest distance
            distance, t = heapq.heappop(heap)

            # Skip if already processed
            if self.st[t]:
                continue

            # Mark as processed
            self.st[t] = True

            # Update distances to all neighbors
            i = self.h[t]
            while i != -1:
                j = self.e[i]
                # Relaxation: update distance if shorter path found
                if self.dist[j] > distance + self.w[i]:
                    self.dist[j] = distance + self.w[i]
                    heapq.heappush(heap, (self.dist[j], j))
                i = self.ne[i]

        # Return shortest distance to node n, -1 if unreachable
        return self.dist[n] if self.dist[n] != INF else -1

def main():
    # Read input from stdin
    data = sys.stdin.read().split()
    if not data:
        return

    # Parse number of nodes and edges
    n = int(data[0])
    m = int(data[1])

    # Initialize Dijkstra solver
    solver = Dijkstra()

    # Read and add all edges
    idx = 2
    for _ in range(m):
        a = int(data[idx])
        b = int(data[idx + 1])
        c = int(data[idx + 2])
        idx += 3
        solver.add_edge(a, b, c)

    # Compute and output shortest path
    result = solver.dijkstra(n)
    print(result)

if __name__ == "__main__":
    main()