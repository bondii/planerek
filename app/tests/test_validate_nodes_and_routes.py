import unittest
from app.scripts.database.PostgresClient import PostgresClient
from app.scripts.database.crud_operations import (
    get_all_edges,
    get_all_nodes,
    get_node_from_id,
    get_node_from_external_id,
)
from app.scripts.node_operations import (
    plot_nodes,
    read_nodes_as_dataframe,
    read_all_nodes_from_csv,
)
from app.scripts.edge_operations import plot_edges, read_all_edges_from_csv


class TestNodePlacement(unittest.TestCase):
    def test_validate_nodes_and_map_csv(self) -> None:

        nodes = read_all_nodes_from_csv()
        edges = read_all_edges_from_csv()
        nodes_df = read_nodes_as_dataframe()

        fig, ax = plot_nodes(nodes)
        fig, ax = plot_edges(edges, nodes_df, fig, ax)

        fig.savefig("nodes_plot_csv.jpg")

    def test_validate_migration_correct_nodes(self) -> None:
        # Done, igration nodes done
        nodes = get_all_nodes(PostgresClient())
        nodes_csv = read_all_nodes_from_csv()

        self.assertEqual(len(nodes), len(nodes_csv))
        for node in nodes:
            found_node = False
            for node_csv in nodes_csv:

                if (
                    node.row + node.column + "_" + str(node.number)
                    == node_csv.id
                ):
                    found_node = True
                    self.assertEqual(node.north, node_csv.north)
                    self.assertEqual(node.east, node_csv.east)
                    self.assertEqual(node.mamsl, node_csv.mamsl)

            self.assertTrue(found_node)

    def test_validate_migration_correct_edges(self) -> None:
        # Also done. Migration is edges done.
        pg_client = PostgresClient()
        edges = get_all_edges(pg_client)
        edges_csv = read_all_edges_from_csv()

        self.assertEqual(len(edges), len(edges_csv))
        for edge in edges:
            found_edge = False
            for edge_csv in edges_csv:

                start_node = get_node_from_id(pg_client, edge.start_node_id)
                end_node = get_node_from_id(pg_client, edge.end_node_id)

                START_NODE_ID_OLD_FORMAT = (
                    start_node.row
                    + start_node.column
                    + "_"
                    + str(start_node.number)
                )
                END_NODE_ID_OLD_FORMAT = (
                    end_node.row + end_node.column + "_" + str(end_node.number)
                )
                if (
                    START_NODE_ID_OLD_FORMAT == edge_csv.start_node
                    and END_NODE_ID_OLD_FORMAT == edge_csv.end_node
                ):
                    found_edge = True
                    self.assertEqual(edge.distance, edge_csv.distance)
                    self.assertEqual(edge.incline, edge_csv.incline)

            self.assertTrue(found_edge)
