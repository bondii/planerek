import unittest
from app.scripts.node_operations import (
    plot_nodes,
    read_nodes_as_dataframe,
    read_all_nodes_from_csv,
)
from app.scripts.edge_operations import plot_edges, read_all_edges_from_csv


class TestNodeplacemant(unittest.TestCase):
    def test_validate_nodes_and_map_csv(self) -> None:

        nodes = read_all_nodes_from_csv()
        edges = read_all_edges_from_csv()
        nodes_df = read_nodes_as_dataframe()

        fig, ax = plot_nodes(nodes)
        fig, ax = plot_edges(edges, nodes_df, fig, ax)

        fig.savefig("nodes_plot_csv.jpg")
