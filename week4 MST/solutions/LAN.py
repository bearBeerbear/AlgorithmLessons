"""
Kruskal's Algorithm for finding Maximum Spanning Tree
This code actually finds the total weight of edges NOT in the MST
by calculating: total_weight - MST_weight

Steps:
1. Calculate total weight of all edges
2. Find MST using Kruskal's algorithm
3. Subtract MST weight from total weight to get removed edges weight

Note: This implementation finds the weight of edges that would be removed
to form an MST, not the MST weight itself.
"""

def find(p, x):
    """Find root with path compression"""
    if p[x] != x:
        p[x] = find(p, p[x])
    return p[x]

def merge(p, x, y):
    """Union two sets"""
    p[find(p, x)] = find(p, y)

def kruskal(n, m, edges):
    """
    Kruskal's algorithm implementation

    Args:
        n: number of vertices
        m: number of edges
        edges: list of tuples (x, y, z) representing edges

    Returns:
        Weight of the Minimum Spanning Tree
    """
    # Initialize parent array for Union-Find
    p = [i for i in range(n + 1)]

    # Sort edges by weight in ascending order
    edges.sort(key=lambda e: e[2])

    ans = 0  # MST weight
    cnt = n - 1  # Need n-1 edges for MST

    # Process edges in sorted order
    for x, y, z in edges:
        if cnt == 0:  # Already have enough edges
            break

        # Check if vertices are in different sets
        if find(p, x) != find(p, y):
            cnt -= 1
            ans += z
            merge(p, x, y)

    return ans

def main():
    # Read input
    n, m = map(int, input().split())
    edges = []
    total_weight = 0

    # Read edges and calculate total weight
    for _ in range(m):
        x, y, z = map(int, input().split())
        edges.append((x, y, z))
        total_weight += z

    # Calculate MST weight using Kruskal
    mst_weight = kruskal(n, m, edges)

    # Output the weight of removed edges (total - MST)
    print(total_weight - mst_weight)

if __name__ == "__main__":
    main()