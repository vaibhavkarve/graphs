from __future__ import annotations

from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from collections.abc import Set as AbstractSet

    from graphs.graph import Graph
    from graphs.symgraph import SymGraph


class GraphError(Exception):
    pass


class NotInVertexSetError[T](GraphError):
    def __init__(
        self, graph: Graph[T] | SymGraph[T], vertex: T, edge: AbstractSet[T]
    ) -> None:
        msg: str = (
            f"Edge {edge} is incident on {vertex = }, which "
            f"is not part of the graph's vertexset {graph.vertices}."
        )
        super().__init__(msg)


class EdgeSizeError[T](GraphError):
    def __init__(self, graph: Graph[T] | SymGraph[T], edge: AbstractSet[T]) -> None:
        relation: str = "more" if len(edge) > graph.EDGE_SIZE else "less"
        msg: str = (
            f"Edge '{set(edge)}' incident on {relation} than "
            "{Graph.EDGE_SIZE} vertices: {list(edge)}."
        )
        super().__init__(msg)
