import sys


def main():
    # Problem: Find the first false statement in a sequence of parity constraints
    # Approach:
    # 1. Use prefix sum: s[i] = a[1] + a[2] + ... + a[i]
    # 2. A constraint [l, r] with 'even' means s[r] - s[l-1] is even → s[r] and s[l-1] have same parity
    # 3. A constraint [l, r] with 'odd' means s[r] - s[l-1] is odd → s[r] and s[l-1] have different parity
    # 4. Use union-find with two domains: regular (same parity) and offset (different parity)
    # 5. For each constraint, check consistency and stop at first contradiction

    data = sys.stdin.read().split()
    if not data:
        return

    n = int(data[0])
    m = int(data[1])

    # Union-Find setup:
    # p[i] represents same parity group for coordinate i
    # p[i + offset] represents different parity group for coordinate i
    offset = 10000  # Enough space to avoid overlap

    # Initialize union-find array
    p = list(range(2 * offset + 1))

    # Coordinate compression map
    coord_map = {}
    coord_count = 0

    def find(x):
        if p[x] != x:
            p[x] = find(p[x])
        return p[x]

    def get_coord(x):
        nonlocal coord_count
        if x not in coord_map:
            coord_count += 1
            coord_map[x] = coord_count
        return coord_map[x]

    result = m  # Default: all constraints are valid

    idx = 2  # Start reading constraints from index 2 in data
    for i in range(1, m + 1):
        a = int(data[idx]);
        idx += 1
        b = int(data[idx]);
        idx += 1
        op = data[idx];
        idx += 1

        # Map coordinates using compression
        # Note: we use a-1 and b to represent s[a-1] and s[b]
        coord_a = get_coord(a - 1)
        coord_b = get_coord(b)

        # Find representatives for both coordinates in both domains
        pa = find(coord_a)
        pb = find(coord_b)
        pa_opposite = find(coord_a + offset)
        pb_opposite = find(coord_b + offset)

        if op == 'even':
            # Same parity constraint
            if pa_opposite == pb:
                # Contradiction: should be same parity but found different parity
                result = i - 1
                break
            # Union: a and b have same parity, and their opposites also have same parity
            p[pa_opposite] = pb_opposite
            p[pa] = pb
        else:
            # 'odd' - different parity constraint
            if pa == pb:
                # Contradiction: should be different parity but found same parity
                result = i - 1
                break
            # Union: a has same parity as b's opposite, and vice versa
            p[pa_opposite] = pb
            p[pa] = pb_opposite

    print(result)


if __name__ == "__main__":
    main()