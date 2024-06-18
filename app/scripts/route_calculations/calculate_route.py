import uuid
from app.dtypes.Route import Route
from app.dtypes.edges import EdgeTable
from app.dtypes.nodes import NodeTable

from app.scripts.route_calculations.Dijkstras import (
    ShortestPathAnd2ndShortestDijkstras,
)


def get_node_to_index_look_up_table(
    nodes: list[NodeTable],
) -> dict[uuid.uuid4, int]:
    return {node.id: idx for idx, node in enumerate(nodes)}


def get_index_to_node_look_up_table(
    nodes: list[NodeTable],
) -> dict[int, uuid.uuid4]:
    return {idx: node.id for idx, node in enumerate(nodes)}


def get_distance_and_incline_adjecency_matrices(
    nodes: list[NodeTable],
    edges: list[EdgeTable],
    node_id_to_index_lookup: dict[uuid.uuid4, int],
) -> tuple[list[list[float]], list[list[float]]]:
    n = len(nodes)
    adjacency_matrix_distance = [[0 for _ in range(n)] for _ in range(n)]
    adjacency_matrix_incline = [[0 for _ in range(n)] for _ in range(n)]

    for edge in edges:
        start_idx = node_id_to_index_lookup[edge.start_node_id]
        end_idx = node_id_to_index_lookup[edge.end_node_id]
        # Gettig strange mypi error here
        adjacency_matrix_distance[start_idx][end_idx] = edge.distance
        adjacency_matrix_distance[end_idx][start_idx] = edge.distance

        # This is wrong, one way should be inclinee, the other decline??
        adjacency_matrix_incline[start_idx][end_idx] = edge.incline
        adjacency_matrix_incline[end_idx][start_idx] = edge.incline

    return adjacency_matrix_distance, adjacency_matrix_incline


def calculate_shortest_and_2nd_shortest_route(
    start_node: NodeTable,
    end_node: NodeTable,
    nodes: list[NodeTable],
    adjecency_matrix: list[list[float]],
    node_id_to_index_lookup: dict[uuid.uuid4, int],
) -> tuple[Route]:
    dijkstras = ShortestPathAnd2ndShortestDijkstras()
    dijkstras.shortestPath(
        adjacencyMatrix=adjecency_matrix,
        src=node_id_to_index_lookup[start_node.id],
        dest=node_id_to_index_lookup[end_node.id],
    )
    index_to_node_lookup = get_index_to_node_look_up_table(nodes)
    node_ids_shortest_path = [
        index_to_node_lookup[node_index] for node_index in dijkstras.path
    ]
    nodes_shortest_path = []
    for node_id in node_ids_shortest_path:
        for node in nodes:
            if node.id == node_id:
                nodes_shortest_path.append(node)
                continue
    # Doesnt work lol

    # dijkstras.find2ndShortest(
    #     adjacencyMatrix=adjecency_matrix,
    #     src=node_id_to_index_lookup[start_node.id],
    #     dest=node_id_to_index_lookup[end_node.id],
    # )
    # node_ids_2nd_shortest_path = [
    #     index_to_node_lookup[node_index] for node_index in dijkstras.path
    # ]
    # nodes_2nd_shortest_path = []
    # for node_id in node_ids_2nd_shortest_path:
    #     for node in nodes:
    #         if node.id == node_id:
    #             nodes_2nd_shortest_path.append(node)
    #             continue

    return Route(nodes=nodes_shortest_path)
