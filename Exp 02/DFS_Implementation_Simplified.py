def dfs(graph, current, visited):
    visited.add(current)
    print(current,end=" ")
    for neighbour in graph[current]:
        if neighbour not in visited:
            dfs(graph,neighbour,visited)
    
graph = {
    'A':['B','C'],
    'B':['A','D','E'],
    'C':['A'],
    'D':['B'],
    'E':['B']
}
visited=set()
dfs(graph,'A',visited)

'''
A B D E C 
'''
