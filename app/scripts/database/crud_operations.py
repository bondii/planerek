import uuid
from app.dtypes.nodes import NodeTable
from app.dtypes.edges import EdgeTable
from app.scripts.database.PostgresClient import PostgresClient


def get_node_from_external_id(
    pg_client: PostgresClient, row: str, column: str, number: int
) -> NodeTable | None:
    with pg_client.get_session() as session:
        node = (
            session.query(NodeTable)
            .filter_by(row=row, column=column, number=number)
            .one_or_none()
        )

        return node


def get_node_from_id(
    pg_client: PostgresClient, id: uuid.UUID
) -> NodeTable | None:
    with pg_client.get_session() as session:
        node = session.query(NodeTable).filter_by(id=id).one_or_none()

        return node


def get_all_nodes(pg_client: PostgresClient) -> list[NodeTable]:
    with pg_client.get_session() as session:
        nodes = session.query(NodeTable).all()

        return nodes


def get_all_nodes_from_edge():
    pass


def get_all_edges(pg_client: PostgresClient) -> list[EdgeTable]:
    with pg_client.get_session() as session:
        edges = session.query(EdgeTable).all()
        return edges


def post_node(pg_client: PostgresClient, node: NodeTable) -> None:
    with pg_client.get_session() as session:
        session.add(node)
        session.commit()


def post_edge(pg_client: PostgresClient, edge: EdgeTable) -> None:
    with pg_client.get_session() as session:
        session.add(edge)
        session.commit()
