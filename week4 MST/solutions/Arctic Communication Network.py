"""
Kruskal-based algorithm to find the (k+1)-th largest edge
when connecting n points into k clusters

Problem Analysis:
- We have n points with coordinates (x,y)
- We want to divide them into k connected clusters
- Using Kruskal's algorithm, when we stop at (n-k) edges added,
  the last edge added is the maximum edge within the k-cluster configuration
- This edge represents the minimum required communication range to connect
  all points into k clusters

Algorithm Steps:
1. Calculate all pairwise distances between points
2. Sort edges by distance in ascending order
3. Use Kruskal to add edges until we have (n-k) edges
4. The last added edge is our answer - the minimum communication range
"""

import math

def find(f, x):
    """Find with path compression"""
    if f[x] != x:
        f[x] = find(f, f[x])
    return f[x]

def calculate_distance(a, b):
    """Calculate Euclidean distance between two points"""
    return math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)

def main():
    # Read input
    n, k = map(int, input().split())
    points = []

    # Read point coordinates
    for i in range(n):
        x, y = map(int, input().split())
        points.append((x, y))

    # Initialize Union-Find
    f = [i for i in range(n)]

    # Generate all possible edges with distances
    edges = []
    for i in range(n):
        for j in range(i + 1, n):
            dist = calculate_distance(points[i], points[j])
            edges.append((i, j, dist))

    # Sort edges by distance in ascending order
    edges.sort(key=lambda x: x[2])

    edges_added = 0
    result = 0.0

    # Kruskal's algorithm
    for u, v, dist in edges:
        root_u = find(f, u)
        root_v = find(f, v)

        # If not in same component, add the edge
        if root_u != root_v:
            f[root_u] = root_v
            edges_added += 1

            # When we have exactly (n-k) edges, we've formed k clusters
            # The last added edge is the maximum edge in this configuration
            if edges_added == n - k:
                result = dist
                break
            # If k=1 (all points connected), we need all n-1 edges
            elif edges_added == n - 1:
                result = dist
                break

    # Output result with 2 decimal places
    print(f"{result:.2f}")

if __name__ == "__main__":
    main()