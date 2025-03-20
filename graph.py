import numpy as np

class Graph:
    def __init__(self, vertices):
        self.connections = np.zeros((vertices, vertices), dtype=int)
        self.vertices = vertices

    def vertices_count(self):
        return self.vertices

    def connect(self, sub_set):
        vertex_1 = sub_set[0]
        vertex_2 = sub_set[1]

        # Vertex already has connection
        if self.is_connected(vertex_1, vertex_2):
            print('Already connected')
            return

        # Vertex index is more than total vertices
        if (vertex_1 or vertex_2) >= self.vertices:
            print('One or more vertices do not exist')
            return

        # Connect vertices
        self.connections[vertex_1, vertex_2] = 1
        self.connections[vertex_2, vertex_1] = 1

    def is_connected(self, v1, v2):
        return (self.connections[v1, v2] == 1) and (self.connections[v2, v1] == 1)

    def is_hamiltonian_util(self, curr_v, path, visited):
        # Base case
        if len(path) == self.vertices:
            return True

        for next_v in range(self.vertices):
            if self.is_connected(curr_v, next_v) and not visited[next_v]:
                path.append(next_v)
                visited[next_v] = True # Mark vertex as visited

                # Recur with next vertex
                if self.is_hamiltonian_util(next_v, path, visited):
                    return True

                # Backtrack if no path exists
                path.pop()
                visited[next_v] = False

        return False # No hamiltonian path found

    def is_hamiltonian(self): # TODO: return path as {a, b, c} str format
        path = []
        visited = [False] * self.vertices  # visited nodes

        # Start at vertex 0)
        for start in range(self.vertices):
            path.append(start)
            visited[start] = True

            if self.is_hamiltonian_util(start, path, visited):
                formatted_path = "{" + ", ".join(num_to_letter(v) for v in path) + "}"
                print("Hamiltonian Path Exists:", formatted_path)
                return True

            # Backtrack if no path found from this start node
            path.pop()
            visited[start] = False

        print("No Hamiltonian Path found")
        return False

    def get_unique_edges(self):
        edges = []
        repeat = set() # Sum of vertex index will always be unique

        for i in range(self.vertices): # Node row and its connections
            for j in range(1, self.vertices): # Avoid self connection

                # Check connection and repeat
                if self.is_connected(i, j) and not i + j in repeat:
                    edges.append([i, j])
                    repeat.add(i + j)

        return np.array(edges)

    def get_degrees(self):
        return np.sum(self.connections, axis=1)

    # TODO: add print function
    # Returns numpy array of vertex number with the smallest degree
    def get_smallest_degree(self):
        degrees = self.get_degrees()  # Get the degree of each vertex
        min_degree = np.min(degrees)  # Find the minimum degree
        min_indices = np.where(degrees == min_degree)[0]  # Get indices of vertices with that degree
        return min_degree, min_indices

    # Returns formatted string set of vertices
    def vertex_str(self):
        return f'{{{", ".join(num_to_letter(v) for v in range(self.vertices))}}}'

    # Returns formatted string set of edges
    def edge_str(self):
        return "{{" + "}, {".join(f"{num_to_letter(a)}, {num_to_letter(b)}" for a, b in self.get_unique_edges()) + "}}"

    def print_connection_array(self):
        print(self.connections)

    def print_vertices(self):
        print('V=' + self.vertex_str())

    def print_edges(self):
        print('E=' + self.edge_str())

    def print_graph(self):
        graph_str = 'G=(' + self.vertex_str() + ',' + self.edge_str() + ')'
        print(graph_str)

# Converts vertex int to letter
def num_to_letter(num):
    return chr(97 + num)

