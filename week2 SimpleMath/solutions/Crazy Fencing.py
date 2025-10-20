"""
Problem: Calculate the total area of N trapezoidal planks in a fence.
Approach:
1. Each plank i has left height h[i], right height h[i+1], and width w[i].
2. The area of plank i = width * (left_height + right_height) / 2.
3. Sum all plank areas and output with one decimal place.
"""

def main():
    import sys

    # Read all input data
    data = sys.stdin.read().split()
    idx = 0

    N = int(data[idx]); idx += 1
    h = list(map(int, data[idx:idx + N + 1])); idx += N + 1
    w = list(map(int, data[idx:idx + N])); idx += N

    total_area = 0.0
    for i in range(N):
        # Area of trapezoid = average of heights * width
        area = w[i] * (h[i] + h[i + 1]) / 2.0
        total_area += area

    # Output with one decimal place
    print(f"{total_area:.1f}")

if __name__ == "__main__":
    main()