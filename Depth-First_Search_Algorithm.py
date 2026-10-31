def dfs(adj_matrix, node):
    stack = []
    visited = []

    # Start with the node passed to the function
    stack.append(node)

    while stack:

        # Take the last node added to the stack
        current = stack.pop()

        # Don't visit a node twice
        if current in visited:
            continue

        # Mark the current node as visited
        visited.append(current)

        # Get all connections of the current node
        neighbors = adj_matrix[current]

        # Check every possible neighbor
        for neighbor, connection in enumerate(neighbors):

            # If an edge exists and the node isn't visited
            if connection == 1 and neighbor not in visited:
                stack.append(neighbor)

    return visited


adj_matrix = [
    [0, 1, 1, 0],
    [1, 0, 0, 1],
    [1, 0, 0, 1],
    [0, 1, 1, 0]
]

print(dfs(adj_matrix, 0))

