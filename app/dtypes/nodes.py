from dataclasses import dataclass
import uuid
from sqlalchemy import UUID, Column, Integer, String, UniqueConstraint
from sqlalchemy.ext.declarative import declarative_base


@dataclass
class Node_old:
    id: str
    north: int
    east: int
    mamsl: int
    comment: str = None


Base = declarative_base()


class NodeTable(Base):
    __tablename__ = "nodes"
    id = Column(UUID, primary_key=True, default=uuid.uuid4)
    row = Column(String(length=5), nullable=False)
    column = Column(String(length=5), nullable=False)
    number = Column(Integer, nullable=False)
    north = Column(Integer, nullable=False)
    east = Column(Integer, nullable=False)
    mamsl = Column(Integer)
    comment = Column(String(length=256))

    __table_args__ = (
        UniqueConstraint(
            "row", "column", "number", name="nodes_row_col_num_unique"
        ),
    )
