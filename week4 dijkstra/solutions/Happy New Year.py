"""
Traveling Salesman Problem on Key Nodes using Dijkstra

Problem: Find the shortest path that visits 6 specific nodes (including node 1) in any order.
The path must start at node 1 and visit all other 5 key nodes with minimum total distance.

Approach:
1. Precompute shortest paths between all pairs of the 6 key nodes using Dijkstra
2. Generate all permutations of the visiting order for the 5 non-start nodes
3. For each permutation, calculate total distance:
   dist[start][node2] + dist[node2][node3] + ... + dist[node5][node6]
4. Find the permutation with minimum total distance

Complexity:
- 6 × Dijkstra runs: O(6 × (M log N))
- 5! = 120 permutations to check
- Efficient for N=50000, M=200000 with this approach
"""

import heapq
import sys
from itertools import permutations

INF = 0x3f3f3f3f


class Graph:
    def __init__(self, n):
        self.n = n
        self.graph = [[] for _ in range(n + 1)]

    def add_edge(self, a, b, c):
        self.graph[a].append((b, c))
        self.graph[b].append((a, c))  # undirected graph

    def dijkstra(self, start, dist):
        """Run Dijkstra from start node and store distances in dist array"""
        # Initialize distance array
        for i in range(len(dist)):
            dist[i] = INF
        dist[start] = 0

        # Priority queue: (distance, node)
        heap = []
        heapq.heappush(heap, (0, start))
        visited = [False] * (self.n + 1)

        while heap:
            current_dist, u = heapq.heappop(heap)

            if visited[u]:
                continue
            visited[u] = True

            for v, weight in self.graph[u]:
                if dist[v] > current_dist + weight:
                    dist[v] = current_dist + weight
                    heapq.heappush(heap, (dist[v], v))


def main():
    data = sys.stdin.read().split()
    idx = 0

    n = int(data[idx]);
    idx += 1  # number of nodes
    m = int(data[idx]);
    idx += 1  # number of edges

    graph = Graph(n)

    # Read key nodes: first key node is always 1, then read 5 more
    key_nodes = [1]  # id[1] = 1
    for i in range(5):
        key_nodes.append(int(data[idx]));
        idx += 1

    # Read edges
    for _ in range(m):
        a = int(data[idx]);
        idx += 1
        b = int(data[idx]);
        idx += 1
        c = int(data[idx]);
        idx += 1
        graph.add_edge(a, b, c)

    # Precompute distances between all pairs of key nodes
    num_key_nodes = 6
    dist_matrix = [[INF] * (n + 1) for _ in range(num_key_nodes + 1)]

    # Run Dijkstra from each key node
    for i in range(1, num_key_nodes + 1):
        graph.dijkstra(key_nodes[i - 1], dist_matrix[i])

    # Generate all permutations of the 5 non-start nodes
    # Nodes are indexed 2-6 in the original, which correspond to indices 1-5 in our 0-based list
    node_indices = list(range(1, 6))  # [1, 2, 3, 4, 5] representing indices in key_nodes

    min_total_distance = INF

    # Try all permutations of visiting order for the 5 non-start nodes
    for perm in permutations(node_indices):
        # Start from node 0 (which is key node 1)
        total_distance = 0
        current_node = 0  # start from first key node (index 0 in key_nodes)

        # Visit each node in the permutation
        for next_node_idx in perm:
            next_node = next_node_idx  # index in key_nodes
            # Get distance from current key node to next key node
            # dist_matrix uses 1-based indexing for the source nodes
            distance = dist_matrix[current_node + 1][key_nodes[next_node]]
            total_distance += distance
            current_node = next_node

        if total_distance < min_total_distance:
            min_total_distance = total_distance

    print(min_total_distance)


if __name__ == "__main__":
    main()