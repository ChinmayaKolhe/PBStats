import heapq

def heuristic(a, b):
    """
    Manhattan Distance Heuristic
    """
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def astar(maze, start, goal):
    rows, cols = len(maze), len(maze[0])

    # Priority queue (min-heap) for A*
    open_set = []
    heapq.heappush(open_set, (0, start))

    # Store cost from start to current node
    g_cost = {start: 0}

    # Parent dictionary to reconstruct path
    parent = {start: None}

    # Movement directions (up, down, left, right)
    directions = [(0,1), (0,-1), (1,0), (-1,0)]

    while open_set:
        _, current = heapq.heappop(open_set)

        if current == goal:
            # Reconstruct shortest path
            path = []
            while current:
                path.append(current)
                current = parent[current]
            return path[::-1]

        x, y = current

        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            # Check boundaries and obstacles
            if 0 <= nx < rows and 0 <= ny < cols and maze[nx][ny] == 0:
                new_cost = g_cost[current] + 1  # Cost of moving to neighbor
                
                if (nx, ny) not in g_cost or new_cost < g_cost[(nx, ny)]:
                    g_cost[(nx, ny)] = new_cost
                    f_cost = new_cost + heuristic((nx, ny), goal)
                    parent[(nx, ny)] = current
                    heapq.heappush(open_set, (f_cost, (nx, ny)))

    return None  # No path found

# Example Maze (0 = free, 1 = wall)
maze = [
    [0, 0, 0, 1, 0],
    [1, 1, 0, 1, 0],
    [0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 1, 0]
]

start = (0, 0)
goal = (4, 4)

path = astar(maze, start, goal)

print("Shortest Path using A*:", path)
