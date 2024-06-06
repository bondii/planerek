from dataclasses import dataclass
from dtypes.noderelated import Node


@dataclass
class Route:
    distance: float  # km
    incline: int  # m
    start_node: Node
    end_node: Node
    difficulty: int = None
    comment: str = None
