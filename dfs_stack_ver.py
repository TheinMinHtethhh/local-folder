def dfs_iterative(graph, start):
    visited = set()  # To track visited nodes
    stack = [start]  # Stack to hold nodes to visit

    while stack:
        node = stack.pop()  # Pop the last node added to the stack
        if node not in visited:
            visited.add(node)  # Mark the node as visited
            print(node)  # Process the node (you can do other operations here)

            # Push all unvisited neighbors to the stack
            for neighbor in reversed(graph[node]):  # Reversed to process left to right
                if neighbor not in visited:#ma shi tte hr ko pl plus tr for eg B has neighbour A , D and E but a is already in visited so only D and E are added to stack
                    stack.append(neighbor)
    print(visited)

# Example graph
graph = {
    'A': ['B', 'C'],#reverse function change the 
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

# Starting DFS iteratively from node 'A'
dfs_iterative(graph, 'A')
def result():
    try:
        return 19
    
    finally:
        return 20
print(result())
