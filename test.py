import unittest
from graph import Graph

class TestGraph(unittest.TestCase):

    def setUp(self):
        # Create a graph with 5 vertices
        self.g = Graph(5)

        # Add edges: {a, a}, {a, b}, {b, c}, {c, d}, {d, d}
        self.g.connect([0, 0])  # loop on a
        self.g.connect([0, 1])  # a - b
        self.g.connect([1, 2])  # b - c
        self.g.connect([2, 3])  # c - d
        self.g.connect([3, 3])  # loop on d

    def test_vertices_count(self):
        self.assertEqual(self.g.vertices_count(), 5)

    def test_edge_count(self):
        edges = self.g.get_unique_edges()
        expected_edges = [[0, 0], [0, 1], [1, 2], [2, 3], [3, 3]]
        self.assertEqual(len(edges), len(expected_edges))
        for edge in expected_edges:
            self.assertIn(edge, edges.tolist())

    def test_degrees(self):
        degrees = self.g.get_degrees()
        expected_degrees = [3, 2, 2, 3, 0]  # a:3, b:2, c:2, d:3, e:0
        self.assertTrue((degrees == expected_degrees).all())

    def test_euler_path(self):
        self.assertTrue(self.g.has_euler_path())

    def test_euler_circuit(self):
        self.assertFalse(self.g.has_euler_circuit())

    def test_smallest_degree(self):
        min_degree, indices = self.g.get_smallest_degree()
        self.assertEqual(min_degree, 0)
        self.assertIn(4, indices)

    def test_connection_matrix(self):
        matrix = self.g.connection_matrix()
        self.assertEqual(matrix.shape, (5, 5))
        self.assertEqual(matrix[0][0], 1)  # loop on a
        self.assertEqual(matrix[3][3], 1)  # loop on d
        self.assertEqual(matrix[0][1], 1)  # a - b

    def test_hamiltonian_output(self):
        # This doesn't return a value, but prints. We'll just check it's callable.
        self.assertIsInstance(self.g.is_hamiltonian(), bool)


if __name__ == "__main__":
    unittest.main()
