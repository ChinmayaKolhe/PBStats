def aStarAlgo(start_node, end_node):
    open_set = set([start_node])
    closed_set = set()

    g = {}
    parents = {}

    g[start_node] = 0
    parents[start_node] = start_node

    while open_set:
        n = None
        # Find node in open set with lowest f(n) = g(n) + h(n)
        for v in open_set:
            if n is None or g[v] + heuristic(v) < g[n] + heuristic(n):
                n = v

        if n is None:
            print("Path does not exist")
            return None

        if n == end_node:
            path = []

            while parents[n] != n:
                path.append(n)
                n = parents[n]

            path.append(start_node)
            path.reverse()
            print('Path found: {}'.format(path))
            return path

        for (m, weight) in get_neighbors(n):
            if m not in open_set and m not in closed_set:
                open_set.add(m)
                parents[m] = n
                g[m] = g[n] + weight
            else:
                if g[m] > g[n] + weight:
                    g[m] = g[n] + weight
                    parents[m] = n

                    if m in closed_set:
                        closed_set.remove(m)
                        open_set.add(m)

        open_set.remove(n)
        closed_set.add(n)

    print("Path does not exist")
    return None

def get_neighbors(v):
    if v in Graph_node:
        return Graph_node[v]
    else:
        return []

def heuristic(n):
    heuristic_dist = {
        'A': 11, 'B': 6, 'C': 99, 'D': 1, 'E': 7, 'G': 0
    }
    return heuristic_dist.get(n, float('inf'))

Graph_node = {
    'A': [('B', 2), ('E', 3)],
    'B': [('C', 1), ('G', 9)],
    'C': [],
    'E': [('D', 6)],
    'D': [('G', 1)],
    'G': []
}

# Run the algorithm
aStarAlgo('A', 'G')

