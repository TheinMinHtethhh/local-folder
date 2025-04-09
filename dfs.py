def dfs(graph, start, visited=None):
    # Initialize the 'visited' set if it's the first call
    if visited is None:
        visited = set()  # This is where we track visited nodes (to avoid cycles)
    
    visited.add(start)  # Mark the current node as visited
    print(start)  # Process the node (in this case, we're just printing it)

    # Recur for all the neighbors of the current node
    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)  # Recursively call dfs for unvisited neighbors

# Example graph (adjacency list)
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

# Starting DFS from node 'A'
dfs(graph, 'A')
list = [1,2,3,4]
list.pop(2)
print(list)
popp = list.pop(1)
print(popp)