"""
Problem: Count triangles from points on a circle that contain the origin.
Approach:
1. Use complementary counting: total triangles minus triangles that don't contain origin.
2. A triangle doesn't contain origin if all three points lie in some semicircle (max arc <= C/2).
3. For each point i, count how many points are in the semicircle starting from i (including diameter endpoints).
4. Subtract triangles where all points are within a semicircle.
5. Special handling for even C to avoid overcounting diameter endpoints.
"""

import sys


def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    c = int(data[1])
    p = list(map(int, data[2:2 + n]))

    # cnt array for counting occurrences of each position (with circular duplication)
    cnt = [0] * (2 * c)
    for i in range(n):
        cnt[p[i]] += 1
        cnt[p[i] + c] += 1  # Duplicate for circular processing

    # Prefix sum array for efficient range queries
    s = [0] * (2 * c)
    s[0] = cnt[0]
    for i in range(1, 2 * c):
        s[i] = s[i - 1] + cnt[i]

    # Total number of possible triangles = C(n, 3)
    res = n * (n - 1) * (n - 2) // 6

    # Subtract triangles that don't contain origin (all points in some semicircle)
    for i in range(c):
        if not cnt[i]:
            continue

        t = cnt[i]  # Number of points at position i
        # Sum of points in semicircle starting from i (including diameter endpoints)
        sum_points = s[i + c // 2] - s[i]

        # Case 1: All three points are at position i
        if t >= 3:
            res -= t * (t - 1) * (t - 2) // 6

        # Case 2: Two points at position i, one in semicircle
        if t >= 2:
            res -= t * (t - 1) // 2 * sum_points

        # Case 3: One point at position i, two in semicircle
        res -= cnt[i] * sum_points * (sum_points - 1) // 2

    # Special handling for even C: we overcounted diameter cases
    # Need to add back triangles where points are exactly on diameter endpoints
    if c % 2 == 0:
        for i in range(c // 2):
            u = cnt[i]  # Points at position i
            v = cnt[i + c // 2]  # Points at opposite end of diameter

            # Two points at opposite end, one at i
            if v >= 2:
                res += u * v * (v - 1) // 2
            # Two points at i, one at opposite end
            if u >= 2:
                res += v * u * (u - 1) // 2

    print(res)


if __name__ == "__main__":
    main()