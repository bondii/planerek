import csv
import os
from typing import List, Optional, Tuple
from matplotlib import pyplot as plt
from matplotlib.axes import Axes
from matplotlib.figure import Figure
import pandas as pd
from app.dtypes.nodes import NodeTable
from app.dtypes.edges import Edge_old


EDGE_CSV = os.path.join(os.getcwd(), "database_csv", "edges_manual.csv")


def calculate_reverse_edge(
    node_a: NodeTable, node_b: NodeTable, edge_AB: Edge_old
) -> Edge_old:
    # Legacy function, not used atm. Will convert it to correct datatype tho
    """
    Assume going node_A --> node_B
    dec_AB = inc_AB-delta_h, where delta_h = mamsl_node_B - mamsl_node_A

    """

    return Edge_old(
        distance=edge_AB.distance,
        incline=edge_AB.incline - (node_b.mamsl - node_a.mamsl),
        start_node=node_b,
        end_node=node_a,
    )


def read_all_edges_from_csv() -> List[Edge_old]:
    # Legacy function, not used atm
    edge_list = []

    with open(EDGE_CSV, newline="", encoding="ISO-8859-1") as f:
        has_header = csv.Sniffer().has_header(f.read(1024))
        f.seek(0)  # Rewind.

        reader = csv.reader(f, delimiter=";")
        if has_header:
            next(reader)
        for row in reader:
            edge_list.append(
                Edge_old(
                    start_node=row[1],
                    end_node=row[2],
                    distance=float(row[3].replace(",", ".")),
                    incline=int(row[4]),
                    comment=row[6],
                )
            )

    return edge_list


def plot_edges(
    edges: List[Edge_old],
    nodes_df: pd.DataFrame,
    fig: Optional[Figure] = None,
    ax: Optional[Axes] = None,
) -> Tuple[Figure, Axes]:
    # Legacy function, not used atm
    if not fig and not ax:
        fig, ax = plt.subplots(figsize=(20, 20))

    for edge in edges:
        node_A_coord = nodes_df.loc[
            nodes_df["id"] == edge.start_node, ["north", "east"]
        ]
        node_B_coord = nodes_df.loc[
            nodes_df["id"] == edge.end_node, ["north", "east"]
        ]

        if len(node_A_coord) > 1:
            print(
                f"WARNING!! There are multiple sets of node {edge.start_node}"
            )
        elif len(node_B_coord) > 1:
            print(f"WARNING!! There are multiple sets of node {edge.end_node}")

        ax.plot(
            (node_A_coord["east"], node_B_coord["east"]),
            (node_A_coord["north"], node_B_coord["north"]),
        )

        middle_of_line = (
            abs(
                node_A_coord["east"].values[0] + node_B_coord["east"].values[0]
            )
            / 2,
            abs(
                node_A_coord["north"].values[0]
                + node_B_coord["north"].values[0]
            )
            / 2,
        )

        ax.text(
            middle_of_line[0], middle_of_line[1], edge.distance, fontsize=12
        )
    return fig, ax
