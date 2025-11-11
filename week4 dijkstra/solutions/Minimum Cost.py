"""
Maximum Reliability Path Problem using Modified Dijkstra

Problem: Find the path between two nodes that maximizes the product of reliability factors.
Each edge has a reliability percentage (100-c)% representing the fraction that passes through.

Approach:
1. Transform the problem: instead of minimizing distance, we maximize the product of reliability factors
2. Use a modified Dijkstra algorithm that:
   - Starts with reliability 1.0 at source
   - Uses max-heap behavior (simulated with negative values) or linear search
   - Updates reliability as: new_reliability = current_reliability * edge_reliability
3. The result is 100 / max_reliability to get the minimum required initial value

Key insight:
- Convert percentage reliability to decimal multipliers (e.g., 95% -> 0.95)
- Find path that maximizes product of multipliers
- Final answer = 100 / best_reliability_product
"""

import sys

def main():
    # Read all input
    data = sys.stdin.read().split()
    idx = 0

    n = int(data[idx]); idx += 1  # number of nodes
    m = int(data[idx]); idx += 1  # number of edges

    # Initialize graph with zeros (0 means no connection)
    g = [[0.0] * (n + 1) for _ in range(n + 1)]

    # Read edges and build graph
    for _ in range(m):
        a = int(data[idx]); idx += 1
        b = int(data[idx]); idx += 1
        c = int(data[idx]); idx += 1  # percentage loss

        # Convert to reliability factor: (100 - c)%
        reliability = (100 - c) / 100.0

        # Store maximum reliability for each edge (graph is undirected)
        g[a][b] = max(g[a][b], reliability)
        g[b][a] = max(g[b][a], reliability)

    st = int(data[idx]); idx += 1  # start node
    ed = int(data[idx]); idx += 1  # end node

    # Dijkstra-like algorithm for maximum reliability path
    dist = [0.0] * (n + 1)  # maximum reliability to reach each node
    vis = [False] * (n + 1)  # visited nodes

    # Start with reliability 1.0 at source
    dist[st] = 1.0

    for _ in range(n):
        # Find unvisited node with maximum reliability
        t = -1
        for j in range(1, n + 1):
            if not vis[j] and (t == -1 or dist[j] > dist[t]):
                t = j

        # If no reachable node found or reached destination, break
        if t == -1 or dist[t] == 0:
            break

        vis[t] = True

        # Update reliability for all neighbors
        for j in range(1, n + 1):
            if g[t][j] > 0:  # If there's a connection
                # New reliability = current reliability * edge reliability
                new_reliability = dist[t] * g[t][j]
                if new_reliability > dist[j]:
                    dist[j] = new_reliability

    # Calculate result: 100 / best_reliability
    # This gives the minimum required initial value to get 100 at destination
    result = 100.0 / dist[ed]
    print(f"{result:.8f}")

if __name__ == "__main__":
    main()