from __future__ import annotations

from typing import Final

from sympy.sets.sets import FiniteSet

from graphs.exceptions import EdgeSizeError, NotInVertexSetError


class SymGraph[T]:
    """A symbolic finite graph."""

    EDGE_SIZE: Final[int] = 2

    def __init__(self, vertices: FiniteSet[T], edges: FiniteSet[FiniteSet[T]]) -> None:
        self.vertices: FiniteSet[T] = vertices
        self.edges: FiniteSet[FiniteSet[T]] = edges
        # Validation:
        for edge in self.edges:
            for vertex in edge:
                if vertex not in self.vertices:
                    raise NotInVertexSetError(self, vertex, edge)
        for edge in self.edges:
            if len(edge) != self.EDGE_SIZE:
                raise EdgeSizeError(self, edge)

    @staticmethod
    def from_edgeset(edges: FiniteSet[FiniteSet[T]]) -> SymGraph[T]:
        vertices: FiniteSet[T] = FiniteSet(
            *[vertex for edge in edges for vertex in edge]
        )
        return SymGraph(vertices=vertices, edges=edges)

    def __repr__(self) -> str:
        return f"SymGraph(vertices={set(self.vertices)}, edges=" + str(
            {str(set(e)) for e in self.edges},
        ).replace("'", "")
