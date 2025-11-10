from collections import deque

# Function to print the puzzle state
def print_puzzle(state):
    for i in range(0, 9, 3):
        print(state[i:i+3])
    print()

# Function to get all possible moves from the current state
def get_neighbors(state):
    neighbors = []
    index = state.index('0')  # '0' represents the blank space
    moves = {
        0: [1, 3],
        1: [0, 2, 4],
        2: [1, 5],
        3: [0, 4, 6],
        4: [1, 3, 5, 7],
        5: [2, 4, 8],
        6: [3, 7],
        7: [4, 6, 8],
        8: [5, 7]
    }

    for move in moves[index]:
        new_state = list(state)
        new_state[index], new_state[move] = new_state[move], new_state[index]
        neighbors.append(''.join(new_state))
    return neighbors

# BFS algorithm to find the solution
def bfs(start, goal):
    visited = set()
    queue = deque([(start, [start])])  # store (state, path)

    while queue:
        state, path = queue.popleft()
        if state == goal:
            return path  # found the solution
        if state in visited:
            continue
        visited.add(state)
        for neighbor in get_neighbors(state):
            if neighbor not in visited:
                queue.append((neighbor, path + [neighbor]))
    return None

# -------- Main Code --------
start = "123405678"   # 0 represents blank space
goal = "123456780"

print("Initial State:")
print_puzzle(start)
print("Goal State:")
print_puzzle(goal)

solution = bfs(start, goal)

if solution:
    print("\nSteps to solve:")
    for step in solution:
        print_puzzle(step)
else:
    print("No solution found!")
