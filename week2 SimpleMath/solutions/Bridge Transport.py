"""
Problem: Find maximum number of train cars that can pass a 40m bridge with weight limit W.
Key points:
- Each car is 10m long, bridge is 40m long → at most 4 cars on bridge at once
- When car i is on bridge, cars i, i-1, i-2, i-3 are on bridge (if they exist)
- We need to ensure sum of weights of these 4 cars ≤ W for all i

Approach:
1. Read weights of all cars
2. For each car i, check sum of weights of cars i, i-1, i-2, i-3
3. If sum > W at any point, maximum cars = i-1
4. If all checks pass, maximum cars = N
"""


def main():
    import sys
    input = sys.stdin.read
    data = input().split()

    W = int(data[0])  # Bridge weight limit
    N = int(data[1])  # Number of cars
    w = [0] * (N + 5)  # Weight array with padding for boundary handling

    # Read car weights
    idx = 2
    for i in range(1, N + 1):
        w[i] = int(data[idx])
        idx += 1

    k = N  # Maximum cars we can keep (initialize to all cars)

    # Check each position where a car is fully on the bridge
    for i in range(1, N + 1):
        total = w[i]  # Current car weight

        # Add weights of previous 3 cars if they exist
        if i - 1 >= 1:
            total += w[i - 1]
        if i - 2 >= 1:
            total += w[i - 2]
        if i - 3 >= 1:
            total += w[i - 3]

        # If weight exceeds limit, we can only keep up to i-1 cars
        if total > W:
            k = i - 1
            break

    print(k)


if __name__ == "__main__":
    main()