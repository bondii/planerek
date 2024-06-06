import csv
import os
from typing import List, Optional, Tuple
from matplotlib import pyplot as plt
from matplotlib.axes import Axes

from matplotlib.figure import Figure
import pandas as pd
from dtypes.noderelated import Node
from dtypes.routes import Route


ROUTE_CSV = os.path.join(os.getcwd(), "database_csv", "routes_manual.csv")


def calculate_reverse_route(
    node_a: Node, node_b: Node, route_AB: Route
) -> Route:
    """
    Assume going node_A --> node_B
    dec_AB = inc_AB-delta_h, where delta_h = mamsl_node_B - mamsl_node_A

    """

    return Route(
        distance=route_AB.distance,
        incline=route_AB.incline - (node_b.mamsl - node_a.mamsl),
        start_node=node_b,
        end_node=node_a,
    )


def read_routes_from_csv() -> List[Route]:
    route_list = []

    with open(ROUTE_CSV, newline="", encoding="ISO-8859-1") as f:
        has_header = csv.Sniffer().has_header(f.read(1024))
        f.seek(0)  # Rewind.

        reader = csv.reader(f, delimiter=";")
        if has_header:
            next(reader)  # Skip header row.
        for row in reader:
            route_list.append(
                Route(
                    start_node=row[1],
                    end_node=row[2],
                    distance=float(row[3].replace(",", ".")),
                    incline=int(row[4]),
                )
            )

    return route_list


def plot_routes(
    routes: List[Route],
    nodes_df: pd.DataFrame,
    fig: Optional[Figure] = None,
    ax: Optional[Axes] = None,
) -> Tuple[Figure, Axes]:
    if not fig and not ax:
        fig, ax = plt.subplots(figsize=(20, 20))

    for route in routes:
        node_A_coord = nodes_df.loc[
            nodes_df["id"] == route.start_node, ["north", "east"]
        ]
        node_B_coord = nodes_df.loc[
            nodes_df["id"] == route.end_node, ["north", "east"]
        ]

        if len(node_A_coord) > 1:
            print(
                f"WARNING!! There are multiple sets of node {route.start_node}"
            )
        elif len(node_B_coord) > 1:
            print(f"WARNING!! There are multiple sets of node {route.end_node}")

        ax.plot(
            (node_A_coord["east"], node_B_coord["east"]),
            (node_A_coord["north"], node_B_coord["north"]),
        )

        middle_of_line = (
            abs(node_A_coord["east"].values[0] + node_B_coord["east"].values[0])
            / 2,
            abs(
                node_A_coord["north"].values[0]
                + node_B_coord["north"].values[0]
            )
            / 2,
        )

        ax.text(
            middle_of_line[0], middle_of_line[1], route.distance, fontsize=12
        )
    return fig, ax
