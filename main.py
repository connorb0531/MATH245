from graph import *
from visual import *

# Graph initialization
vertex_count = 5
g = Graph(vertex_count)

# Graph edge creation
g.connect([0, 1])
g.connect([1, 2])
g.connect([0, 0])
g.connect([3, 2])
g.connect([3, 3])

# Print graph info
g.print_vertices() # vertex set
g.print_edges() # edge set
g.print_graph() # graph set
print('Connection matrix:', g.connection_matrix()) # connection matrix

# Degrees
print('Degree array: ', g.get_degrees())
print('Smallest degree array: ', g.get_smallest_degree()) # [smallest degree, vertices who have such]

# Paths/circuits
print('Euler path: ', g.has_euler_path())
print('Euler circuit: ', g.has_euler_circuit())
g.is_hamiltonian()

# Graphical display
draw_graph(g)