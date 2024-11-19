def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()  # Initialize the visited set on the first call

    print(start, end=" ")  # Process the current node (e.g., print it)
    visited.add(start)  # Mark the current node as visited

    # Explore each neighbor of the current node
    for neighbor in graph[start]:
        if neighbor not in visited:  # If the neighbor hasn't been visited
            dfs(graph, neighbor, visited)  # Recursively perform DFS on the neighbor

# Example Usage:
# Define the graph as an adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

print("DFS traversal starting from node 'A':")
dfs(graph, 'A')

'''
DFS traversal starting from node 'A':
A B D E F C 
'''
