from dataclasses import dataclass
import uuid
from dtypes.nodes import Node_old, NodeTable
from sqlalchemy import FLOAT, UUID, Column, ForeignKey, String, UniqueConstraint
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base


@dataclass
class Route_old:
    distance: float  # km
    incline: int  # m
    start_node: Node_old
    end_node: Node_old
    difficulty: int = None
    comment: str = None


Base = declarative_base()


class RouteTable(Base):
    __tablename__ = "routes"
    id = Column(UUID, primary_key=True, default=uuid.uuid4)
    start_node_id = Column(UUID, ForeignKey(NodeTable.id), nullable=False)
    end_node_id = Column(UUID, ForeignKey(NodeTable.id), nullable=False)
    distance = Column(FLOAT, nullable=False)
    incline = Column(FLOAT, nullable=False)
    decline = Column(FLOAT, nullable=True)
    trail_type = Column(String(length=256))

    __table_args__ = (
        UniqueConstraint(
            "start_node", "end_node", name="routes_start_node_end_node_unique"
        ),
    )
