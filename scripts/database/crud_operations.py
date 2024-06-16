from dtypes.nodes import NodeTable
from dtypes.routes import RouteTable
from scripts.database.PostgresClient import PostgresClient


def get_node(
    pg_client: PostgresClient, row: str, column: str, number: int
) -> NodeTable | None:
    with pg_client.get_session() as session:
        node = (
            session.query(NodeTable)
            .filter_by(row=row, column=column, number=number)
            .one_or_none()
        )

        return node


def get_all_nodes(pg_client: PostgresClient) -> list[NodeTable]:
    with pg_client.get_session() as session:
        nodes = session.query(NodeTable).all()

        return nodes


def get_all_nodes_from_route():
    pass


def get_all_routes(pg_client: PostgresClient) -> list[RouteTable]:
    with pg_client.get_session() as session:
        nodes = session.query(NodeTable).all()
        return nodes


def post_node(pg_client: PostgresClient, node: NodeTable) -> None:
    with pg_client.get_session() as session:
        session.add(node)
        session.commit()


def post_route(pg_client: PostgresClient, route: RouteTable) -> None:
    with pg_client.get_session() as session:
        session.add(route)
        session.commit()
