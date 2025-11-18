"""
Union-Find (Disjoint Set Union) Data Structure Implementation

Problem: Handle dynamic connectivity queries - check if two elements are connected
and union operations to connect elements.

Approach:
1. Use Union-Find data structure with path compression
2. Each set has a representative (root) element
3. Find operation: find the root of an element with path compression
4. Union operation: merge two sets by making one root point to the other

Complexity:
- Nearly O(1) per operation with path compression and union by rank
- Without union by rank: O(log n) per operation worst case
"""

import sys

class UnionFind:
    def __init__(self, n):
        """
        Initialize Union-Find data structure with n elements

        Args:
            n: number of elements, elements are numbered from 1 to n
        """
        self.parent = list(range(n + 1))  # 1-based indexing

    def find(self, x):
        """
        Find the root of element x with path compression

        Args:
            x: element to find root of

        Returns:
            Root element of x
        """
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # Path compression
        return self.parent[x]

    def union(self, a, b):
        """
        Union the sets containing elements a and b

        Args:
            a, b: elements to union
        """
        root_a = self.find(a)
        root_b = self.find(b)
        if root_a != root_b:
            self.parent[root_a] = root_b

    def connected(self, a, b):
        """
        Check if elements a and b are in the same set

        Args:
            a, b: elements to check

        Returns:
            True if a and b are connected, False otherwise
        """
        return self.find(a) == self.find(b)

def main():
    data = sys.stdin.read().split()
    idx = 0

    n = int(data[idx]); idx += 1  # number of elements
    m = int(data[idx]); idx += 1  # number of operations

    uf = UnionFind(n)

    results = []

    for _ in range(m):
        op = data[idx]; idx += 1
        a = int(data[idx]); idx += 1
        b = int(data[idx]); idx += 1

        if op == "M":
            # Union operation: connect elements a and b
            uf.union(a, b)
        else:  # "Q" or any query operation
            # Query operation: check if a and b are connected
            if uf.connected(a, b):
                results.append("Yes")
            else:
                results.append("No")

    # Output all results
    print("\n".join(results))

if __name__ == "__main__":
    main()