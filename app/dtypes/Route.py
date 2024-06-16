from dataclasses import dataclass
from pydantic import BaseModel
from app.dtypes.nodes import NodeTable


@dataclass
class Route:
    nodes: list[NodeTable]
