from collections import deque

def bfs_shortest_path(maze, start, goal):
    rows = len(maze)
    cols = len(maze[0])

    directions = [(0,1), (0,-1), (1,0), (-1,0)]

    queue = deque([start])
    visited = set([start])
    
    # To reconstruct path
    parent = {start: None}

    while queue:
        x, y = queue.popleft()

        # If goal is found, reconstruct path
        if (x, y) == goal:
            path = []
            curr = goal
            while curr:
                path.append(curr)
                curr = parent[curr]
            path.reverse()
            return path  # Shortest path

        # Explore neighbors
        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            # Check bounds and obstacles
            if 0 <= nx < rows and 0 <= ny < cols:
                if maze[nx][ny] == 0 and (nx, ny) not in visited:
                    visited.add((nx, ny))
                    parent[(nx, ny)] = (x, y)
                    queue.append((nx, ny))

    return None  # No path found


maze = [
    [0, 0, 1, 0],
    [1, 0, 1, 0],
    [0, 0, 0, 0],
    [0, 1, 1, 0]
]

start = (0, 0)
goal = (3, 3)

path = bfs_shortest_path(maze, start, goal)
print("Shortest Path:", path)
