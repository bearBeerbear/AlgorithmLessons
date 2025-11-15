"""
Kruskal's Algorithm for Minimum Spanning Tree (MST)

Steps:
1. Sort all edges by weight in ascending order
2. Initialize Union-Find (Disjoint Set Union) data structure
3. Iterate through sorted edges:
   a. For each edge, check if two vertices are in different sets
   b. If they are, add edge to MST and union the two sets
4. Check if we have exactly n-1 edges in MST

Time Complexity: O(m log m) for sorting + O(m α(n)) for Union-Find
Space Complexity: O(n + m)
"""

def find(p, a):
    """Find the root of element a with path compression"""
    if p[a] != a:
        p[a] = find(p, p[a])
    return p[a]

def kruskal(n, m, edges):
    """
    Kruskal's algorithm to find Minimum Spanning Tree

    Args:
        n: number of vertices
        m: number of edges
        edges: list of (a, b, w) representing edges

    Returns:
        Total weight of MST or -1 if no MST exists
    """
    # Initialize parent array for Union-Find
    parent = [i for i in range(n + 1)]

    # Sort edges by weight in ascending order
    edges.sort(key=lambda x: x[2])

    res = 0  # Total weight of MST
    cnt = 0  # Number of edges in MST

    # Process each edge in sorted order
    for a, b, w in edges:
        # Find roots of both vertices
        root_a = find(parent, a)
        root_b = find(parent, b)

        # If vertices are in different sets, add edge to MST
        if root_a != root_b:
            res += w
            cnt += 1
            # Union the two sets
            parent[root_a] = root_b

    # Check if we have a spanning tree (n-1 edges)
    if cnt != n - 1:
        return -1  # No MST exists
    return res

def main():
    # Read input
    n, m = map(int, input().split())
    edges = []
    for _ in range(m):
        a, b, c = map(int, input().split())
        edges.append((a, b, c))

    # Calculate MST using Kruskal's algorithm
    result = kruskal(n, m, edges)

    # Output result
    if result == -1:
        print("impossible")
    else:
        print(result)

if __name__ == "__main__":
    main()