import sys

def main():
    # Problem: Check consistency of equality and inequality constraints using Union-Find
    # Approach:
    # 1. Discretize all variables using coordinate compression
    # 2. Sort constraints by type (equality constraints first)
    # 3. Process equality constraints to union variables
    # 4. Check inequality constraints - if any two variables in inequality constraint are in same set, it's inconsistent

    input_data = sys.stdin.read().strip().split()
    t = int(input_data[0])
    idx = 1
    results = []

    for _ in range(t):
        n = int(input_data[idx]); idx += 1
        constraints = []
        coord_map = {}
        coord_count = 0

        # Read all constraints and map coordinates
        for i in range(n):
            x = int(input_data[idx]); idx += 1
            y = int(input_data[idx]); idx += 1
            e = int(input_data[idx]); idx += 1
            constraints.append((x, y, e))

            # Map coordinates to sequential indices
            if x not in coord_map:
                coord_count += 1
                coord_map[x] = coord_count
            if y not in coord_map:
                coord_count += 1
                coord_map[y] = coord_count

        # Initialize Union-Find data structure
        parent = list(range(coord_count + 1))

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        # Sort constraints: equality constraints (e=1) first
        constraints.sort(key=lambda x: x[2], reverse=True)

        consistent = True

        # Process constraints
        for x, y, e in constraints:
            mapped_x = coord_map[x]
            mapped_y = coord_map[y]

            root_x = find(mapped_x)
            root_y = find(mapped_y)

            if e == 1:
                # Equality constraint: union the sets
                if root_x != root_y:
                    parent[root_x] = root_y
            else:
                # Inequality constraint: check if they are in different sets
                if root_x == root_y:
                    consistent = False
                    break

        results.append("YES" if consistent else "NO")

    # Output all results
    print("\n".join(results))

if __name__ == "__main__":
    main()