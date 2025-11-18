# Problem: Determine the judge in a rock-paper-scissors game using union-find with 3 domains (self, eat, enemy)
# Approach:
# 1. Use union-find data structure with 3 domains per player: self, eat, enemy (like in food chain problem)
# 2. For each player as candidate judge, check consistency of all statements excluding those involving the judge
# 3. '=' means same gesture: merge self domains, eat domains, enemy domains
# 4. '>' means x beats y: merge x's self with y's enemy, x's eat with y's self, x's enemy with y's eat
# 5. Track the first line where contradiction occurs for each candidate judge
# 6. If exactly one candidate has no contradictions, they are the judge

class UnionFind:
    def __init__(self, n):
        # Initialize union-find with size n
        self.parent = list(range(n))
        self.size = [1] * n

    def find(self, x):
        # Find root with path compression
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        # Union by size
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x == root_y:
            return
        if self.size[root_x] < self.size[root_y]:
            self.parent[root_x] = root_y
            self.size[root_y] += self.size[root_x]
        else:
            self.parent[root_y] = root_x
            self.size[root_x] += self.size[root_y]


def main():
    import sys

    while True:
        try:
            # Read n and m
            line = sys.stdin.readline().strip()
            if not line:
                break
            n, m = map(int, line.split())

            # Store all operations
            operations = []
            x_vals = []
            y_vals = []

            for k in range(m):
                line = sys.stdin.readline().strip()
                # Parse the line: format is "x op y"
                parts = line.split()
                if len(parts) == 3:
                    # Format: "x op y" with spaces
                    x_val = int(parts[0])
                    op_char = parts[1]
                    y_val = int(parts[2])
                else:
                    # Format: "xopy" without spaces - need to extract operator
                    # Find the operator position
                    op_pos = -1
                    for i, char in enumerate(line):
                        if char in ['=', '<', '>']:
                            op_pos = i
                            break
                    if op_pos == -1:
                        # No operator found, skip this line
                        continue
                    x_val = int(line[:op_pos])
                    op_char = line[op_pos]
                    y_val = int(line[op_pos + 1:])

                x_vals.append(x_val)
                operations.append(op_char)
                y_vals.append(y_val)

            # line[i] stores first contradictory line for candidate i
            line_contradiction = [0] * n
            cnt = 0  # Count of valid candidates
            ans_p = 0  # Judge candidate index
            ans_l = 0  # Maximum line number

            # Try each candidate as judge
            for i in range(n):
                uf = UnionFind(3 * n)  # 3 domains: self, eat, enemy
                valid = True

                for k in range(m):
                    x_val = x_vals[k]
                    y_val = y_vals[k]
                    op_char = operations[k]

                    # Skip if statement involves current judge candidate
                    if x_val == i or y_val == i:
                        continue

                    # Calculate indices for 3 domains
                    x_self = x_val
                    x_eat = x_val + n
                    x_enemy = x_val + 2 * n

                    y_self = y_val
                    y_eat = y_val + n
                    y_enemy = y_val + 2 * n

                    if op_char == '=':
                        # Check for contradiction: x shouldn't beat y or y shouldn't beat x
                        if (uf.find(x_eat) == uf.find(y_self) or
                                uf.find(x_enemy) == uf.find(y_self)):
                            valid = False
                            line_contradiction[i] = k + 1  # 1-indexed line number
                            break
                        else:
                            # Merge all three domains
                            uf.union(x_self, y_self)
                            uf.union(x_eat, y_eat)
                            uf.union(x_enemy, y_enemy)
                    elif op_char == '>':
                        # Check for contradiction: x and y shouldn't be same, and y shouldn't beat x
                        if (uf.find(x_self) == uf.find(y_self) or
                                uf.find(y_eat) == uf.find(x_self)):
                            valid = False
                            line_contradiction[i] = k + 1  # 1-indexed line number
                            break
                        else:
                            # Merge according to predator-prey relationship
                            uf.union(x_self, y_enemy)  # x's self == y's enemy
                            uf.union(x_eat, y_self)  # x's eat == y's self
                            uf.union(x_enemy, y_eat)  # x's enemy == y's eat
                    elif op_char == '<':
                        # Swap x and y for '<' operation
                        # Check for contradiction: x and y shouldn't be same, and x shouldn't beat y
                        if (uf.find(y_self) == uf.find(x_self) or
                                uf.find(x_eat) == uf.find(y_self)):
                            valid = False
                            line_contradiction[i] = k + 1  # 1-indexed line number
                            break
                        else:
                            # Merge according to predator-prey relationship (swapped)
                            uf.union(y_self, x_enemy)  # y's self == x's enemy
                            uf.union(y_eat, x_self)  # y's eat == x's self
                            uf.union(y_enemy, x_eat)  # y's enemy == x's eat

                if valid:
                    cnt += 1
                    ans_p = i

            # Output results
            if cnt == 0:
                print("Impossible")
            elif cnt == 1:
                # Find maximum line where any candidate was eliminated
                ans_l = max(line_contradiction)
                print(f"Player {ans_p} can be determined to be the judge after {ans_l} lines")
            else:
                print("Can not determine")

        except EOFError:
            break
        except ValueError:
            break


if __name__ == "__main__":
    main()