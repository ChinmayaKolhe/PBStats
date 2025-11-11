# Depth First Search (DFS) in Python

def dfs(graph, start, target, visited=None):
    if visited is None:
        visited = set()  # To avoid revisiting nodes (prevent cycles)

    visited.add(start)  # Mark current node as visited
    print(start, end=" ")  # Visualize traversal order

    # If the target is found, we stop
    if start == target:
        return True

    # Explore neighbors
    for neighbor in graph[start]:
        if neighbor not in visited:
            if dfs(graph, neighbor, target, visited):  # Recursively call DFS
                return True

    return False


# Example Graph (Game Map)
game_map = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

# Starting and Target nodes
start_node = 'A'
target_node = 'F'

print("DFS Traversal Order:")
dfs(game_map, start_node, target_node)