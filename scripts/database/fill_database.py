from dtypes.routes import RouteTable
from scripts.database.PostgresClient import PostgresClient
from scripts.database.crud_operations import get_node, post_node, post_route
from scripts.node_operations import read_all_nodes_from_csv
from dtypes.nodes import NodeTable, Node_old
from scripts.route_operations import read_all_routes_from_csv

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


def reformat_old_route_to_new_node(node_old: Node_old) -> NodeTable:
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


def fill_routes_from_csv(pg_client: PostgresClient) -> None:
    # TODO this need trouble shooting, one route came twice.
    routes_old_format = read_all_routes_from_csv()
    for old_route in routes_old_format:

        start_node = get_node(
            pg_client=pg_client,
            row=old_route.start_node[0],
            column=old_route.start_node[1],
            number=int(old_route.start_node.split("_")[-1]),
        )

        end_node = get_node(
            pg_client=pg_client,
            row=old_route.end_node[0],
            column=old_route.end_node[1],
            number=int(old_route.end_node.split("_")[-1]),
        )

        try:
            post_route(
                pg_client=pg_client,
                route=RouteTable(
                    start_node_id=start_node.id,
                    end_node_id=end_node.id,
                    distance=old_route.distance,
                    incline=old_route.incline,
                    trail_type=old_route.comment,
                ),
            )

        except Exception as e:
            print(e)
