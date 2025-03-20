from graph import Graph

graph = Graph(3)
graph.connect([0, 1])
#graph.connect([1, 2])
#graph.connect([1, 1])

#graph.print_vertices()
#graph.print_edges()
#graph.print_graph()
graph.print_connection_array()

print(graph.get_degrees())
print(graph.get_smallest_degree())


graph.is_hamiltonian()

# TODO: add unit testing