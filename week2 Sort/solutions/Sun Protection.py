# Problem: Maximum matching between intervals and points with quantities
# Approach:
# 1. Read n (number of intervals) and m (number of point types) from first line
# 2. Read intervals (a) and points with quantities (b)
# 3. Sort both lists in descending order by their first value
# 4. For each interval, try to find the largest point that falls within the interval
# 5. If found and the point has remaining quantity, use one and increment count
# 6. Output the total number of successful matches

def main():
    # Read n and m from first line
    first_line = input().split()
    n = int(first_line[0])
    m = int(first_line[1])

    # Read intervals (first, second)
    a = []
    for _ in range(n):
        line = input().split()
        first = int(line[0])
        second = int(line[1])
        a.append((first, second))

    # Read points with quantities (first = point value, second = quantity)
    b = []
    for _ in range(m):
        line = input().split()
        first = int(line[0])
        second = int(line[1])
        b.append((first, second))

    # Sort both lists in descending order by first element
    a.sort(reverse=True)
    b.sort(reverse=True)

    res = 0  # Count of successful matches

    # For each interval, find the best matching point
    for interval in a:
        interval_start, interval_end = interval

        # Check each point type
        for j in range(m):
            point_value, quantity = b[j]

            # Check if point is within interval and has remaining quantity
            if (quantity > 0 and
                    point_value >= interval_start and
                    point_value <= interval_end):
                # Use one point of this type
                res += 1
                b[j] = (point_value, quantity - 1)
                break

    print(res)


if __name__ == "__main__":
    main()