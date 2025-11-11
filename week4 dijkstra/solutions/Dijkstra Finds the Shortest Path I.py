"""
Dijkstra's Algorithm with Adjacency List and Linear Search

Problem: Find the shortest path from node 1 to node n in a directed weighted graph.

Approach:
1. Use adjacency list to represent the graph
2. Implement Dijkstra's algorithm with linear search for the minimum distance node
3. Maintain state array to track nodes with finalized shortest distances
4. Suitable for small graphs (n <= 500)

Complexity: O(n² + m) - efficient for small n
"""

import sys

INF = 0x3f3f3f3f

class Graph:
    def __init__(self, n):
        self.n = n
        self.graph = [[] for _ in range(n + 1)]

    def add_edge(self, a, b, c):
        """Add directed edge from a to b with weight c"""
        self.graph[a].append((b, c))

    def dijkstra(self, start, end):
        """
        Dijkstra's algorithm using linear search for min distance node

        Args:
            start: source node
            end: target node

        Returns:
            Shortest distance from start to end, or -1 if no path exists
        """
        dist = [INF] * (self.n + 1)
        state = [False] * (self.n + 1)  # Track finalized nodes
        dist[start] = 0

        # We need at most n iterations
        for _ in range(self.n):
            # Find unvisited node with minimum distance
            t = -1
            for j in range(1, self.n + 1):
                if not state[j] and (t == -1 or dist[j] < dist[t]):
                    t = j

            # If no reachable node found or reached target, break early
            if t == -1 or dist[t] == INF:
                break

            # Mark node as processed
            state[t] = True

            # Update distances to all neighbors
            for neighbor, weight in self.graph[t]:
                if dist[neighbor] > dist[t] + weight:
                    dist[neighbor] = dist[t] + weight

        return dist[end] if dist[end] != INF else -1

def main():
    data = sys.stdin.read().split()
    idx = 0

    n = int(data[idx]); idx += 1  # number of nodes
    m = int(data[idx]); idx += 1  # number of edges

    graph = Graph(n)

    # Read directed edges
    for _ in range(m):
        a = int(data[idx]); idx += 1
        b = int(data[idx]); idx += 1
        w = int(data[idx]); idx += 1
        graph.add_edge(a, b, w)

    # Find shortest path from node 1 to node n
    result = graph.dijkstra(1, n)
    print(result)

if __name__ == "__main__":
    main()