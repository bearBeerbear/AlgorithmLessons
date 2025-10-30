# Solution Approach:
# BFS to find minimum time from N to K on number line.
# Moves: x → x-1, x → x+1, x → 2*x (all cost 1).
# Use BFS with deque. Limit search space to [0, 200010].
# Early exit when K is reached.

from collections import deque

N, K = map(int, input().split())
MAX = 200010  # Safe upper limit: covers 2*1e5
dist = [-1] * MAX
dist[N] = 0

q = deque([N])

while q:
    x = q.popleft()

    # Found the cow
    if x == K:
        print(dist[x])
        break

    # Try x-1
    if x - 1 >= 0 and dist[x - 1] == -1:
        dist[x - 1] = dist[x] + 1
        q.append(x - 1)

    # Try x+1
    if x + 1 < MAX and dist[x + 1] == -1:
        dist[x + 1] = dist[x] + 1
        q.append(x + 1)

    # Try 2*x (teleport)
    nxt = x * 2
    if nxt < MAX and dist[nxt] == -1:
        dist[nxt] = dist[x] + 1
        q.append(nxt)