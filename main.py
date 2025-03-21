from graph import Graph

# Graph initialization
graph = Graph(3)

# Graph edge creation
graph.connect([0, 1])
graph.connect([1, 2])
graph.connect([1, 1])

# Print graph info
graph.print_vertices() # vertex set
graph.print_edges() # edge set
graph.print_graph() # graph set
graph.print_connection_array() # connection matrix

print(graph.get_degrees()) # Degree count
print(graph.get_smallest_degree()) # Smallest degrees (vertex num)

# Checks for hamiltonian path
graph.is_hamiltonian()