"""
Problem: Solve the Tower of Hanoi puzzle and print the move sequences

Approach:
1. The Tower of Hanoi is a classic recursive problem with three rods (A, B, C)
2. The goal is to move n disks from rod A to rod C using rod B as auxiliary
3. Recursive strategy:
   - Move n-1 disks from A to B using C as auxiliary
   - Move the largest disk from A to C
   - Move n-1 disks from B to C using A as auxiliary
4. Base case: when only 1 disk remains, move it directly from source to destination
"""


def hanoi(n, a, b, c):
    """
    Recursive function to solve Tower of Hanoi and print move sequences

    Args:
        n: number of disks to move
        a: source rod
        b: auxiliary rod
        c: destination rod
    """
    if (n == 1):
        # Base case: move single disk directly from source to destination
        print(a + "->" + str(n) + "->" + c)
    else:
        # Step 1: Move n-1 disks from source to auxiliary using destination as temporary
        hanoi(n - 1, a, c, b)
        # Step 2: Move the largest disk from source to destination
        print(a + "->" + str(n) + "->" + c)
        # Step 3: Move n-1 disks from auxiliary to destination using source as temporary
        hanoi(n - 1, b, a, c)


# Read input: n disks and three rod names
lines = input().split(" ")
n = int(lines[0])  # Number of disks
a = lines[1]  # Source rod name
b = lines[2]  # Auxiliary rod name
c = lines[3]  # Destination rod name

# Solve Tower of Hanoi: move n disks from A to C using B as auxiliary
hanoi(n, a, c, b)