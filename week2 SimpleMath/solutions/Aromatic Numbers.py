'''
Problem: Given N wooden pieces of lengths L_i, we can make planks by joining two pieces (lengths add up).
A fence is made of multiple planks of the same length (height). The fence length = number of planks.
Goal: Find the maximum possible fence length and how many different heights achieve this maximum.

Approach:
1. Count frequency of each piece length (1 to 2000 possible).
2. For each possible plank height H (2 to 4000), count how many pairs of pieces sum to H.
3. For counting pairs:
   - If a = b (same piece length used twice), need at least 2 pieces: add count[a] // 2
   - If a != b, add min(count[a], count[b]) for a < b to avoid double counting
4. Track the maximum number of planks (pairs) and how many heights achieve it.

Complexity: O(max(L)^2) = O(2000^2) = 4M operations, feasible.
'''


def main():
    import sys
    input = sys.stdin.read
    data = input().split()

    N = int(data[0])
    L = list(map(int, data[1:1 + N]))

    # Frequency array for piece lengths (1 to 2000)
    freq = [0] * 4005  # Extended to 4005 to avoid index errors
    for length in L:
        freq[length] += 1

    max_planks = 0  # Maximum number of planks for any height
    heights_count = 0  # Number of heights achieving max_planks

    # Check all possible plank heights H (from 2 to 4000)
    for H in range(2, 4001):
        planks = 0  # Number of planks we can make of height H

        # Try all possible first piece lengths a
        for a in range(1, H):
            b = H - a  # Second piece length
            # Check if b is within valid range
            if b < 1 or b > 4000:
                continue

            if a == b:
                # Same length pieces: need at least 2 pieces of this length
                planks += freq[a] // 2
            else:
                # Different lengths: count pairs without duplication
                if a < b:  # This ensures we count each (a,b) pair only once
                    planks += min(freq[a], freq[b])

        # Update maximum and count
        if planks > max_planks:
            max_planks = planks
            heights_count = 1
        elif planks == max_planks:
            heights_count += 1

    print(max_planks, heights_count)


if __name__ == "__main__":
    main()