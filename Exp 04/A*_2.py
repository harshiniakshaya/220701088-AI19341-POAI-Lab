def aStarAlgo(start_node, stop_node):
    open_set = {start_node}
    g = {start_node: 0}
    parents = {start_node: start_node}
    while open_set:
        n = min(open_set, key=lambda node: g[node] + heuristic(node))
        if n == stop_node:
            path = []
            while parents[n] != n:
                path.append(n)
                n = parents[n]
            path.append(start_node)
            return path[::-1]
        open_set.remove(n)
        for (m, weight) in get_neighbors(n):
            if m not in g or g[m] > g[n] + weight:
                g[m] = g[n] + weight
                parents[m] = n
                open_set.add(m)
    return None

def get_neighbors(v):
    return Graph_nodes.get(v, [])
def heuristic(n):
    return {'A': 11, 'B': 6, 'C': 99, 'D': 1, 'E': 7, 'G': 0}[n]
Graph_nodes = {
    'A': [('B', 2), ('E', 3)],
    'B': [('C', 1), ('G', 9)],
    'E': [('D', 6)],
    'D': [('G', 1)],
}
print(aStarAlgo('A', 'G'))
