"""
Dijkstra's Algorithm with Adjacency Matrix

Problem: Find the shortest path between two nodes in an undirected weighted graph.

Approach:
1. Use adjacency matrix to represent the graph
2. Implement Dijkstra's algorithm with linear search for minimum distance node
3. Suitable for dense graphs where n is small (n <= 2500)

Complexity: O(n²) - efficient for small n, suitable for dense graphs
"""

import sys

INF = 0x3f3f3f3f

def dijkstra_adjacency_matrix(n, st, ed, graph):
    """
    Dijkstra's algorithm using adjacency matrix representation

    Args:
        n: number of nodes
        st: start node
        ed: end node
        graph: n x n adjacency matrix

    Returns:
        Shortest distance from st to ed, or INF if no path exists
    """
    dist = [INF] * (n + 1)
    visited = [False] * (n + 1)
    dist[st] = 0

    for _ in range(n):
        # Find unvisited node with minimum distance
        t = -1
        for j in range(1, n + 1):
            if not visited[j] and (t == -1 or dist[j] < dist[t]):
                t = j

        # If no reachable node found, break early
        if t == -1 or dist[t] == INF:
            break

        visited[t] = True

        # Update distances to all neighbors
        for j in range(1, n + 1):
            if graph[t][j] != INF:  # If there's an edge
                if dist[j] > dist[t] + graph[t][j]:
                    dist[j] = dist[t] + graph[t][j]

    return dist[ed]

def main():
    data = sys.stdin.read().split()
    idx = 0

    n = int(data[idx]); idx += 1  # number of nodes
    m = int(data[idx]); idx += 1  # number of edges
    st = int(data[idx]); idx += 1  # start node
    ed = int(data[idx]); idx += 1  # end node

    # Initialize adjacency matrix with INF (no connection)
    graph = [[INF] * (n + 1) for _ in range(n + 1)]

    # Set diagonal to 0 (distance from node to itself)
    for i in range(1, n + 1):
        graph[i][i] = 0

    # Read edges (undirected graph)
    for _ in range(m):
        a = int(data[idx]); idx += 1
        b = int(data[idx]); idx += 1
        c = int(data[idx]); idx += 1
        # Store minimum weight for multiple edges between same nodes
        if c < graph[a][b]:
            graph[a][b] = c
            graph[b][a] = c

    # Run Dijkstra's algorithm
    result = dijkstra_adjacency_matrix(n, st, ed, graph)

    print(result)

if __name__ == "__main__":
    main()