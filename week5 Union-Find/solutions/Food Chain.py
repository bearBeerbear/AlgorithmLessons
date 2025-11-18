# Problem: Animal relationship validation using union-find with distance modulo 3
# Approach:
# 1. Use union-find with path compression and maintain distance from node to root
# 2. Distance is maintained modulo 3, where:
#    - 0: same type as root
#    - 1: eats root
#    - 2: eaten by root (or equivalently, root eats this node)
# 3. For type 1 claims (same species):
#    - If in same set, check if distance difference is multiple of 3
#    - If not in same set, merge with appropriate distance
# 4. For type 2 claims (x eats y):
#    - If in same set, check if distance from x is 1 more than y modulo 3
#    - If not in same set, merge with appropriate distance

def main():
    import sys

    # Read n and k
    data = sys.stdin.read().split()
    n = int(data[0])
    k = int(data[1])

    # Initialize parent and distance arrays
    parent = list(range(n + 1))  # 1-indexed
    dist = [0] * (n + 1)  # distance from node to root

    def find(x):
        # Find root with path compression and update distance
        if parent[x] != x:
            # Store the root first
            root = find(parent[x])
            # Update distance: add parent's distance
            dist[x] += dist[parent[x]]
            # Path compression
            parent[x] = root
        return parent[x]

    result = 0

    idx = 2  # Start reading from position 2 in data
    for _ in range(k):
        e = int(data[idx]); idx += 1
        x = int(data[idx]); idx += 1
        y = int(data[idx]); idx += 1

        # Check if x or y is out of range
        if x > n or y > n:
            result += 1
            continue

        root_x = find(x)
        root_y = find(y)

        if e == 1:  # x and y are same type
            if root_x == root_y:
                # Check if distance difference is multiple of 3
                if (dist[x] - dist[y]) % 3 != 0:
                    result += 1
            else:
                # Merge sets: make root_x point to root_y
                parent[root_x] = root_y
                # Set distance so that (dist[x] + dist[root_x] - dist[y]) % 3 == 0
                dist[root_x] = (dist[y] - dist[x]) % 3

        else:  # e == 2: x eats y
            if root_x == root_y:
                # x should be 1 more than y modulo 3
                if (dist[x] - dist[y] - 1) % 3 != 0:
                    result += 1
            else:
                # Merge sets: make root_x point to root_y
                parent[root_x] = root_y
                # Set distance so that (dist[x] + dist[root_x] - dist[y]) % 3 == 1
                dist[root_x] = (dist[y] + 1 - dist[x]) % 3

    print(result)

if __name__ == "__main__":
    main()