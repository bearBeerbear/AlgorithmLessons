import sys
import bisect

"""
Problem: Graph Combination with Minimum Spanning Trees
Approach:
1. We have two separate graphs and need to compute a combined cost function
2. For each graph, compute Minimum Spanning Tree (MST) using Kruskal's algorithm
3. The solution involves:
   - Calculating unused edge weights from MST computations
   - Combining results from both graphs with specific multipliers
   - Using prefix sums and binary search for efficient range queries
4. Key steps:
   a) Compute MST for first graph (m nodes, k edges), store MST edge weights
   b) Compute MST for second graph (n nodes, t edges), store MST edge weights  
   c) Calculate base cost using unused edges and fixed multipliers
   d) For each MST edge in second graph, find how many MST edges in first graph 
       have higher weight and compute the adjustment cost
5. Optimizations:
   - Union-Find with path compression for efficient connectivity checks
   - Binary search in sorted MST edges instead of linear scan
   - Prefix sum array for O(1) range sum queries
Time Complexity: O(k log k + t log t + n log m) for sorting and binary searches
Space Complexity: O(n + m) for storing MST edges and prefix sums
"""

def find(x, p):
    if p[x] != x:
        p[x] = find(p[x], p)
    return p[x]

def kruskal_fast(n, edges, w):
    p = list(range(n + 1))
    edges.sort(key=lambda x: x[2])

    unused_sum = 0
    cnt = 0
    for u, v, weight in edges:
        pu = find(u, p)
        pv = find(v, p)
        if pu != pv:
            p[pu] = pv
            cnt += 1
            w[cnt] = weight
        else:
            unused_sum += weight

    return unused_sum

def main_fast():
    import sys
    input = sys.stdin.read().split()
    idx = 0

    n, m, k, t = int(input[idx]), int(input[idx+1]), int(input[idx+2]), int(input[idx+3])
    idx += 4

    # Process first graph
    edges1 = []
    for _ in range(k):
        u, v, w_val = int(input[idx]), int(input[idx+1]), int(input[idx+2])
        idx += 3
        edges1.append((u, v, w_val))

    w1 = [0] * (m + 1)
    unused1 = kruskal_fast(m, edges1, w1)
    ans = unused1 * n

    # Process second graph
    edges2 = []
    sum_weights = 0
    for _ in range(t):
        u, v, w_val = int(input[idx]), int(input[idx+1]), int(input[idx+2])
        idx += 3
        edges2.append((u, v, w_val))
        sum_weights += w_val

    w2 = [0] * (n + 1)
    unused2 = kruskal_fast(n, edges2, w2)
    ans += unused2 + sum_weights * (m - 1)

    # Optimized processing of MST edges
    mst1 = sorted(w1[1:m], reverse=True)
    prefix = [0] * (len(mst1) + 1)
    for i, val in enumerate(mst1):
        prefix[i + 1] = prefix[i] + val

    # Use binary search for counting
    for i in range(1, n):
        target = w2[i]
        # Binary search in descending sorted array
        lo, hi = 0, len(mst1)
        while lo < hi:
            mid = (lo + hi) // 2
            if mst1[mid] >= target:
                lo = mid + 1
            else:
                hi = mid
        cnt = lo

        if cnt > 0:
            ans += prefix[cnt] - target * cnt

    print(ans)

if __name__ == "__main__":
    main_fast()