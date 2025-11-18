"""
Union-Find with Size Tracking

Problem: Handle dynamic connectivity queries with additional operation to get
the size of connected components.

Operations:
1. Connect two elements (union)
2. Check if two elements are connected
3. Get the size of the connected component containing an element

Approach:
1. Extend basic Union-Find with size array
2. Maintain size of each connected component at the root
3. When unioning, update sizes accordingly

Complexity: O(α(n)) per operation (near constant time)
"""

import sys


class UnionFind:
    def __init__(self, n):
        """
        Initialize Union-Find with size tracking

        Args:
            n: number of elements (1 to n)
        """
        self.parent = list(range(n + 1))  # 1-based indexing
        self.size = [1] * (n + 1)  # size of each component

    def find(self, x):
        """
        Find root of x with path compression
        """
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, a, b):
        """
        Union sets containing a and b, update sizes
        Skip if already connected to avoid double counting
        """
        root_a = self.find(a)
        root_b = self.find(b)

        if root_a == root_b:
            return  # Already connected

        # Union by attaching smaller tree to larger tree (optional optimization)
        if self.size[root_a] < self.size[root_b]:
            root_a, root_b = root_b, root_a

        self.parent[root_b] = root_a
        self.size[root_a] += self.size[root_b]

    def connected(self, a, b):
        """
        Check if a and b are in the same component
        """
        return self.find(a) == self.find(b)

    def get_size(self, a):
        """
        Get size of the connected component containing a
        """
        root = self.find(a)
        return self.size[root]


def main():
    data = sys.stdin.read().split()
    idx = 0

    n = int(data[idx]);
    idx += 1
    m = int(data[idx]);
    idx += 1

    uf = UnionFind(n)
    results = []

    for _ in range(m):
        op = data[idx];
        idx += 1

        if op == "C":
            # Connect operation: union a and b
            a = int(data[idx]);
            idx += 1
            b = int(data[idx]);
            idx += 1
            uf.union(a, b)

        elif op == "Q1":
            # Query connectivity: check if a and b are connected
            a = int(data[idx]);
            idx += 1
            b = int(data[idx]);
            idx += 1
            if uf.connected(a, b):
                results.append("Yes")
            else:
                results.append("No")

        else:  # "Q2"
            # Query size: get size of component containing a
            a = int(data[idx]);
            idx += 1
            size = uf.get_size(a)
            results.append(str(size))

    print("\n".join(results))


if __name__ == "__main__":
    main()