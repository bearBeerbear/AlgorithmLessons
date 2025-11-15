import sys


class Info:
    def __init__(self, animal, cost):
        self.animal = animal
        self.cost = cost


def prims(graph, n):
    """
    Prim's algorithm for Minimum Spanning Tree
    """
    INF = 999999999
    unseen = INF
    val = [0] * (n + 1)

    # Initialize val array
    for k in range(1, n + 1):
        val[k] = -unseen
    val[0] = -(unseen + 1)

    min_idx = 1
    k = 0

    while True:
        k = min_idx
        val[k] = -val[k]  # Mark as visited
        min_idx = 0

        if val[k] == unseen:
            val[k] = 0

        # Update distances to neighbors
        for t in range(1, n + 1):
            if val[t] < 0:  # If not visited
                if graph[k - 1][t - 1] != INF and val[t] < -(graph[k - 1][t - 1]):
                    val[t] = -(graph[k - 1][t - 1])
                if val[t] > val[min_idx]:
                    min_idx = t

        if min_idx == 0:
            break

    # Calculate total MST weight
    answer = 0
    for i in range(1, n + 1):
        answer += val[i]
    return answer


def main():
    """
    Problem: Animal Farm - Minimum cost to gather all animals
    Approach:
    1. Model fences as graph where nodes are animals (pens) and outside
    2. Process input to build adjacency matrix with edge costs
    3. Use Prim's algorithm to find MST twice:
       - Once excluding outside area
       - Once including outside area
    4. Answer is the minimum of the two MST weights
    """
    data = sys.stdin.read().split()
    if not data:
        return

    idx = 0
    n = int(data[idx]);
    idx += 1

    # Initialize graph with large values
    INF = 999999999
    graph = [[INF] * (n + 1) for _ in range(n + 1)]
    for i in range(n + 1):
        graph[i][i] = 0

    # Initialize input grid for processing edges
    input_grid = [[Info(-1, 0) for _ in range(1001)] for _ in range(1001)]

    # Process each animal pen
    for i in range(n):
        num_edges = int(data[idx]);
        idx += 1
        corners = []
        costs = []

        # Read corners
        for k in range(num_edges):
            corners.append(int(data[idx]));
            idx += 1

        # Read costs
        for k in range(num_edges):
            costs.append(int(data[idx]));
            idx += 1

        # Process each edge of the pen
        for k in range(num_edges):
            j = (k + 1) % num_edges
            corner1 = corners[k]
            corner2 = corners[j]
            cost_val = costs[k]

            # If this edge was already processed (shared fence)
            if input_grid[corner1][corner2].cost > 0:
                other_animal = input_grid[corner1][corner2].animal
                # Update graph with minimum cost
                if graph[i][other_animal] > cost_val:
                    graph[i][other_animal] = cost_val
                    graph[other_animal][i] = cost_val

                # Mark as processed
                input_grid[corner1][corner2].animal = -1
                input_grid[corner2][corner1].animal = -1
            else:
                # New fence - store in input grid
                input_grid[corner1][corner2].cost = cost_val
                input_grid[corner1][corner2].animal = i
                input_grid[corner2][corner1].cost = cost_val
                input_grid[corner2][corner1].animal = i

    # Process outside edges (edges that still have animal >= 0)
    for i in range(1001):
        for j in range(1001):
            if input_grid[i][j].animal >= 0:
                animal_idx = input_grid[i][j].animal
                cost_val = input_grid[i][j].cost
                # Connect animal to outside (node n)
                if graph[animal_idx][n] > cost_val:
                    graph[animal_idx][n] = cost_val
                    graph[n][animal_idx] = cost_val

    # Calculate MST twice and take minimum
    # MST excluding outside (n nodes: animals 0 to n-1)
    answer1 = prims(graph, n)

    # MST including outside (n+1 nodes: animals 0 to n-1 + outside)
    answer2 = prims(graph, n + 1)

    print(min(answer1, answer2))


if __name__ == "__main__":
    main()