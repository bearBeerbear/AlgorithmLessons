from collections import deque
import sys


def main():
    # Problem: Find the minimum weight threshold such that when we remove all edges with weight <= threshold,
    # the remaining graph is bipartite (can be colored with 2 colors without adjacent nodes having same color)

    # Approach:
    # 1. Use binary search to find the minimum threshold value
    # 2. For each candidate threshold, check if the graph becomes bipartite after removing edges with weight <= threshold
    # 3. Use DFS/BFS to check if the remaining graph (with edges > threshold) is bipartite

    n, m = map(int, sys.stdin.readline().split())

    # Build adjacency list: graph[node] = list of (neighbor, weight)
    graph = [[] for _ in range(n + 1)]

    for _ in range(m):
        a, b, c = map(int, sys.stdin.readline().split())
        graph[a].append((b, c))
        graph[b].append((a, c))

    def is_bipartite(threshold):
        # Check if the graph with edges > threshold is bipartite
        # color array: 0 = uncolored, 1 = color1, 2 = color2
        color = [0] * (n + 1)

        for i in range(1, n + 1):
            if color[i] == 0:
                # Start BFS from uncolored node
                queue = deque([i])
                color[i] = 1

                while queue:
                    node = queue.popleft()

                    for neighbor, weight in graph[node]:
                        # Skip edges with weight <= threshold (considered removed)
                        if weight <= threshold:
                            continue

                        if color[neighbor] == 0:
                            # Color neighbor with opposite color
                            color[neighbor] = 3 - color[node]
                            queue.append(neighbor)
                        elif color[neighbor] == color[node]:
                            # Conflict: adjacent nodes have same color
                            return False
        return True

    # Binary search for minimum threshold
    left, right = 0, 10 ** 9

    while left < right:
        mid = (left + right) // 2

        if is_bipartite(mid):
            # Current threshold works, try smaller threshold
            right = mid
        else:
            # Current threshold doesn't work, need larger threshold
            left = mid + 1

    print(left)


if __name__ == "__main__":
    main()