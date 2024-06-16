from app.dtypes.edges import EdgeTable
from app.scripts.database.PostgresClient import PostgresClient
from app.scripts.database.crud_operations import (
    get_node_from_external_id,
    post_node,
    post_edge,
)
from app.scripts.node_operations import read_all_nodes_from_csv
from app.dtypes.nodes import NodeTable, Node_old
from app.scripts.edge_operations import read_all_edges_from_csv

"""
functions to fill up  postgres database with CSV material
"""


def reformat_old_node_to_new_node(node_old: Node_old) -> NodeTable:
    return NodeTable(
        row=node_old.id[0],
        column=node_old.id[1],
        number=int(node_old.id.split("_")[-1]),
        north=node_old.north,
        east=node_old.east,
        mamsl=node_old.mamsl,
        comment=node_old.comment,
    )


def fill_nodes_from_csv(pg_client: PostgresClient) -> None:
    nodes_old_format = read_all_nodes_from_csv()

    nodes = [reformat_old_node_to_new_node(node) for node in nodes_old_format]

    for node in nodes:
        post_node(pg_client=pg_client, node=node)


def fill_edges_from_csv(pg_client: PostgresClient) -> None:
    edges_old_format = read_all_edges_from_csv()
    for old_edge in edges_old_format:

        start_node = get_node_from_external_id(
            pg_client=pg_client,
            row=old_edge.start_node[0],
            column=old_edge.start_node[1],
            number=int(old_edge.start_node.split("_")[-1]),
        )

        end_node = get_node_from_external_id(
            pg_client=pg_client,
            row=old_edge.end_node[0],
            column=old_edge.end_node[1],
            number=int(old_edge.end_node.split("_")[-1]),
        )

        post_edge(
            pg_client=pg_client,
            edge=EdgeTable(
                start_node_id=start_node.id,
                end_node_id=end_node.id,
                distance=old_edge.distance,
                incline=old_edge.incline,
                trail_type=old_edge.comment,
            ),
        )
