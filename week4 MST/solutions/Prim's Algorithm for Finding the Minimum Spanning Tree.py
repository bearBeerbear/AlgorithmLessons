"""
Prim's Algorithm for Minimum Spanning Tree (MST)

Steps:
1. Initialize all distances to infinity and create visited array
2. Start with first node (distance 0)
3. For each vertex:
   a. Find vertex with minimum distance that hasn't been visited
   b. If not first vertex and distance is INF, graph is disconnected
   c. Add distance to result (except for first vertex)
   d. Update distances of adjacent vertices
   e. Mark vertex as visited

Time Complexity: O(n^2) for adjacency matrix
Space Complexity: O(n^2)
"""

INF = float('inf')

def prim(n, m, edges):
    # Initialize graph with INF
    g = [[INF] * (n + 1) for _ in range(n + 1)]

    # Build adjacency matrix (undirected graph)
    for a, b, c in edges:
        g[a][b] = min(g[a][b], c)
        g[b][a] = min(g[b][a], c)

    # Distance from MST set to each vertex
    dist = [INF] * (n + 1)
    # Track if vertex is in MST
    st = [False] * (n + 1)

    # Initialize first vertex distance
    dist[1] = 0
    res = 0  # Total weight of MST

    # Process all vertices
    for i in range(n):
        # Find vertex with minimum distance not in MST
        t = -1
        for j in range(1, n + 1):
            if not st[j] and (t == -1 or dist[t] > dist[j]):
                t = j

        # If no connection to MST and not first vertex
        if i > 0 and dist[t] == INF:
            return INF

        # Add to result (except for first vertex)
        if i > 0:
            res += dist[t]

        # Update distances of adjacent vertices
        for j in range(1, n + 1):
            if not st[j] and dist[j] > g[t][j]:
                dist[j] = g[t][j]

        # Mark vertex as included in MST
        st[t] = True

    return res

def main():
    # Read input
    n, m = map(int, input().split())
    edges = []
    for _ in range(m):
        a, b, c = map(int, input().split())
        edges.append((a, b, c))

    # Calculate MST using Prim's algorithm
    result = prim(n, m, edges)

    # Output result
    if result == INF:
        print("impossible")
    else:
        print(result)

if __name__ == "__main__":
    main()