"""
Problem: Rearrange coins on stacks with adjacent moves, larger coin cannot be placed on smaller coin.
Approach:
1. Use BFS to explore all possible states.
2. A state is represented as a tuple of tuples (each tuple is a stack of coins from top to bottom).
3. Initial state: each position has one coin as given.
4. Goal state: each position i has exactly coin i.
5. Moves: pick top coin from a stack, move to adjacent stack if valid (target empty or target top coin > moving coin).
6. If goal state is reached, return steps; else IMPOSSIBLE.
"""

from collections import deque


def solve():
    import sys
    input_data = sys.stdin.read().strip().split()
    idx = 0
    results = []
    while True:
        n = int(input_data[idx]);
        idx += 1
        if n == 0:
            break
        initial = list(map(int, input_data[idx:idx + n]));
        idx += n

        # Initial state: list of lists, each list is a stack (top = first element)
        start_state = tuple(tuple([val]) for val in initial)

        # Goal state
        goal_state = tuple(tuple([i]) for i in range(1, n + 1))

        # BFS
        queue = deque()
        queue.append((start_state, 0))
        visited = set()
        visited.add(start_state)

        found = -1

        while queue:
            state, steps = queue.popleft()

            if state == goal_state:
                found = steps
                break

            # Try all possible moves
            for pos in range(n):
                if not state[pos]:  # empty stack
                    continue
                # coin to move
                coin = state[pos][0]
                # move left
                if pos > 0:
                    # check rule: target stack empty or top coin > moving coin
                    if not state[pos - 1] or state[pos - 1][0] > coin:
                        # new state
                        new_stacks = list(list(stack) for stack in state)
                        # remove from pos
                        new_stacks[pos] = list(new_stacks[pos][1:])
                        # add to pos-1
                        new_stacks[pos - 1] = [coin] + new_stacks[pos - 1]
                        new_state = tuple(tuple(stack) for stack in new_stacks)
                        if new_state not in visited:
                            visited.add(new_state)
                            queue.append((new_state, steps + 1))
                # move right
                if pos < n - 1:
                    if not state[pos + 1] or state[pos + 1][0] > coin:
                        new_stacks = list(list(stack) for stack in state)
                        new_stacks[pos] = list(new_stacks[pos][1:])
                        new_stacks[pos + 1] = [coin] + new_stacks[pos + 1]
                        new_state = tuple(tuple(stack) for stack in new_stacks)
                        if new_state not in visited:
                            visited.add(new_state)
                            queue.append((new_state, steps + 1))

        if found == -1:
            results.append("IMPOSSIBLE")
        else:
            results.append(str(found))

    print("\n".join(results))


if __name__ == "__main__":
    solve()