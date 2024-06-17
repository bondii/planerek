from typing import List, Tuple
from app.dtypes.nodes import Node_old
from app.scripts.node_operations import (
    get_index_of_node,
    get_node_from_index,
    plot_nodes,
    read_nodes_as_dataframe,
    read_all_nodes_from_csv,
)
from app.scripts.edge_operations import plot_edges, read_all_edges_from_csv
from app.scripts.shortest_way import ShortestPathAnd2ndShortestDijkstras

edges = read_all_edges_from_csv()
nodes_df = read_nodes_as_dataframe()


def get_adjecency_matrices() -> Tuple[List[List[int]], List[List[int]]]:
    adj_mat_dist = [
        [0 for _ in range(len(nodes_df))] for _ in range(len(nodes_df))
    ]
    adj_mat_inc = [
        [0 for _ in range(len(nodes_df))] for _ in range(len(nodes_df))
    ]

    for edge in edges:
        start_node_index = get_index_of_node(nodes_df, edge.start_node)
        end_node_index = get_index_of_node(nodes_df, edge.end_node)

        adj_mat_dist[start_node_index][end_node_index] = edge.distance
        adj_mat_inc[start_node_index][end_node_index] = edge.incline

        adj_mat_dist[end_node_index][start_node_index] = edge.distance
        adj_mat_inc[end_node_index][start_node_index] = edge.incline

    return adj_mat_dist, adj_mat_inc


def calculate_route(start_id: str, end_id: str) -> None:
    start_node_index = get_index_of_node(nodes_df, start_id)
    end_node_index = get_index_of_node(nodes_df, end_id)

    adj_mat_dist, adj_mat_inc = get_adjecency_matrices()
    dijkstras = ShortestPathAnd2ndShortestDijkstras()
    dijkstras.shortestPath(adj_mat_dist, start_node_index, end_node_index)
    node_list = []
    for node_index in dijkstras.path:
        node_df = get_node_from_index(nodes_df, node_index)

        node_list.append(Node_old(**node_df.to_dict()))

    all_nodes = read_all_nodes_from_csv()
    fig, ax = plot_nodes(all_nodes, color="red")
    fig, ax = plot_edges(edges, nodes_df, fig, ax)
    fig, _ = plot_nodes(node_list, fig, ax, color="blue", dot_size=80)

    fig.savefig("test_dijkstras.jpg")
