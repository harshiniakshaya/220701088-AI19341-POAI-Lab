class Graph:
    def __init__(self, adj_list):
        self.adj_list = adj_list

    def heuristic(self, node):
        # Example heuristic values (can be customized)
        return {'A': 1, 'B': 1, 'C': 1, 'D': 1}.get(node, float('inf'))

    def a_star(self, start, goal):
        to_visit = {start}  # Nodes to explore
        costs = {start: 0}  # Cost to reach each node
        parents = {start: None}  # To reconstruct the path

        while to_visit:
            # Get the node with the smallest estimated total cost
            current = min(to_visit, key=lambda node: costs[node] + self.heuristic(node))

            # If we reached the goal, reconstruct the path
            if current == goal:
                path = []
                while current is not None:
                    path.append(current)
                    current = parents[current]
                return path[::-1]  # Reverse to get path from start to goal

            to_visit.remove(current)

            # Explore neighbors
            for neighbor, weight in self.adj_list.get(current, []):
                new_cost = costs[current] + weight
                if new_cost < costs.get(neighbor, float('inf')):
                    costs[neighbor] = new_cost
                    parents[neighbor] = current
                    to_visit.add(neighbor)

        return None  # Return None if no path is found


# Example usage
adj_list = {
    'A': [('B', 1), ('C', 3), ('D', 7)],
    'B': [('D', 5)],
    'C': [('D', 12)]
}

graph = Graph(adj_list)
path = graph.a_star('A', 'D')
print("Path found:", path)
#Path found: ['A', 'B', 'D']
