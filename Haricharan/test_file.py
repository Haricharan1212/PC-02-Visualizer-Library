"""Testing using test cases"""
import unittest
import networkx as nx
import splitwise


class TestCalc(unittest.TestCase):
    """class inherited from unittest.TestCase"""

    def test_1(self):

        """Defining test 1"""

        graph = nx.DiGraph()
        graph.add_nodes_from(["a", "b", "c", "d"])
        graph.add_edges_from(
            [
                ("a", "b", {"weight": 5}),
                ("b", "c", {"weight": 5}),
                ("c", "a", {"weight": 3}),
                ("d", "a", {"weight": 2}),
            ]
        )
        splitwise.display_graph_and_output(graph)
        # output_graph = splitwise.return_output_graph(graph)

        # correct_output_graph = nx.DiGraph()
        # correct_output_graph.add_nodes_from(["a", "b", "c", "d"])
        # correct_output_graph.add_edges_from(
        #     [
        #         ("a", "b", {"weight": 2}),
        #         ("a", "d", {"weight": 2}),
        #     ]
        # )
        # assert list(output_graph.edges.data()) == list(
        #     correct_output_graph.edges.data()
        # )

    def test_2(self):

        """Defining test 1"""

        graph = nx.DiGraph()
        graph.add_nodes_from(["a", "b", "c", "d"])
        graph.add_edges_from(
            [
                ("a", "b", {"weight": 200}),
                ("b", "c", {"weight": 100}),
                ("c", "d", {"weight": 100}),
                ("d", "a", {"weight": 100}),
            ]
        )
        output_graph = splitwise.return_output_graph(graph)
        correct_output_graph = nx.DiGraph()

        correct_output_graph.add_nodes_from(["a", "b", "c", "d"])
        correct_output_graph.add_edges_from(
            [
                ("a", "b", {"weight": 100}),
            ]
        )
        assert list(output_graph.edges.data()) == list(
            correct_output_graph.edges.data()
        )


if __name__ == "__main__":
    unittest.main(verbosity=0)
