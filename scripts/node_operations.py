import os
from typing import List, Optional, Tuple
import csv
from matplotlib.axes import Axes
import pandas as pd
from matplotlib.figure import Figure
from dtypes.noderelated import Node
import matplotlib.pyplot as plt

NODE_CSV = os.path.join(os.getcwd(), "database_csv", "nodes.csv")


def get_index_of_node(dataframe: pd.DataFrame, node_id: str) -> int:
    return dataframe.index[dataframe["id"] == node_id].values[0]


def get_node_from_index(dataframe: pd.DataFrame, index: str) -> pd.DataFrame:
    return dataframe.iloc[index]


def read_nodes_as_dataframe() -> pd.DataFrame:
    return pd.read_csv(NODE_CSV, encoding="ISO-8859-1", delimiter=";")


def read_nodes_from_csv() -> List[Node]:
    node_list = []

    with open(NODE_CSV, newline="", encoding="ISO-8859-1") as f:
        has_header = csv.Sniffer().has_header(f.read(1024))
        f.seek(0)  # Rewind.

        reader = csv.reader(f, delimiter=";")
        if has_header:
            next(reader)  # Skip header row.
        for row in reader:
            node_list.append(
                Node(
                    id=row[0],
                    north=int(row[1]),
                    east=int(row[2]),
                    mamsl=int(row[3]),
                    comment=row[4],
                )
            )

    return node_list


def plot_nodes(
    nodes: List[Node],
    fig: Optional[Figure] = None,
    ax: Optional[Axes] = None,
    color: Optional[str] = "red",
    dot_size: Optional[int] = 20,
) -> Tuple[Figure, Axes]:
    if not fig and not ax:
        fig, ax = plt.subplots(figsize=(20, 20))

    for node in nodes:
        ax.scatter(node.east, node.north, c=color, s=dot_size)
        ax.text(node.east + 500, node.north, node.id, fontsize=12)
        ax.text(node.east, node.north - 1000, node.comment, fontsize=12)

    return fig, ax
