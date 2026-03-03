BFS Implementation

from collections import deque

def bfs():
    visited = set()
    queue = deque([((0,0), [])])

    while queue:
        (x, y), path = queue.popleft()

        if x == 2:
            return path + [(x,y)]

        if (x,y) in visited:
            continue

        visited.add((x,y))

        next_states = [
            (4, y),      # fill 4L
            (x, 3),      # fill 3L
            (0, y),      # empty 4L
            (x, 0),      # empty 3L
            (x - min(x, 3-y), y + min(x, 3-y)),  # pour 4->3
            (x + min(y, 4-x), y - min(y, 4-x))   # pour 3->4
        ]

        for state in next_states:
            queue.append((state, path + [(x,y)]))

print("BFS Solution:", bfs())

DFS Implementation

def dfs():
    visited = set()
    stack = [((0,0), [])]

    while stack:
        (x, y), path = stack.pop()

        if x == 2:
            return path + [(x,y)]

        if (x,y) in visited:
            continue

        visited.add((x,y))

        next_states = [
            (4, y),
            (x, 3),
            (0, y),
            (x, 0),
            (x - min(x, 3-y), y + min(x, 3-y)),
            (x + min(y, 4-x), y - min(y, 4-x))
        ]

        for state in next_states:
            stack.append((state, path + [(x,y)]))

print("DFS Solution:", dfs())
