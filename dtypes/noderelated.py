from dataclasses import dataclass


@dataclass
class Node:
    id: str
    north: int
    east: int
    mamsl: int
    comment: str = None
