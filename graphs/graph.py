from __future__ import annotations

from collections import deque
from collections.abc import Callable, Iterable, KeysView, Mapping
from typing import Final, Literal

from graphs.exceptions import EdgeSizeError, NotInVertexSetError


type Prop[T] = Callable[[T], bool]


class Graph[T]:
    EDGE_SIZE: Final[int] = 2

    def __init__(self, vertices: Iterable[T], edges: Iterable[Iterable[T]]) -> None:
        self.vertices: frozenset[T] = frozenset(vertices)
        self.edges: frozenset[frozenset[T]] = frozenset(map(frozenset, edges))
        # Test validity only once during initialization.
        for edge in self.edges:
            for vertex in edge:
                if vertex not in self.vertices:
                    raise NotInVertexSetError(self, vertex, edge)
        for edge in self.edges:
            if len(edge) != self.EDGE_SIZE:
                raise EdgeSizeError(self, edge)

    def neighbor_map(self) -> dict[T, frozenset[T]]:
        nmap: dict[T, list[T]] = {v: [] for v in self.vertices}
        for v1, v2 in self.edges:
            nmap[v1].append(v2)
            nmap[v2].append(v1)
        return {v: frozenset(neighbors) for v, neighbors in nmap.items()}

    @staticmethod
    def from_neighbor_map(nmap: Mapping[T, Iterable[T]]) -> Graph[T]:
        vertices: KeysView[T] = nmap.keys()
        edges: list[tuple[T, T]] = [
            (v, v2) for v, neighbors in nmap.items() for v2 in neighbors
        ]
        return Graph(vertices, edges)

    def __repr__(self) -> str:
        return f"Graph(vertices={set(self.vertices)}, edges=" + str(
            {str(set(e)) for e in self.edges},
        ).replace("'", "")

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Graph):
            # Let's assume that both graphs share the same typevar.
            return self.vertices == other.vertices and self.edges == other.edges  # pyright: ignore[reportUnknownMemberType]
        return NotImplemented

    @staticmethod
    def _parent_dict_to_path(
        parent_dict: dict[T, T], start_vertex: T, goal_vertex: T
    ) -> deque[T]:
        path: deque[T] = deque([goal_vertex])
        v: T = goal_vertex

        while v != start_vertex:
            v = parent_dict[v]
            path.appendleft(v)
        return path

    def breadth_first_search(
        self, start_vertex: T, goal: Prop[T]
    ) -> tuple[deque[T], None] | tuple[None, list[T]]:
        assert start_vertex in self.vertices
        processing_queue: deque[T] = deque([start_vertex])
        parent_dict: dict[T, T] = {start_vertex: start_vertex}
        bfs_sequence: list[T] = []
        neighbor_map: dict[T, frozenset[T]] = self.neighbor_map()
        while processing_queue:
            v: T = processing_queue.popleft()
            if goal(v):
                # Goal was found. Useful information in this case is the
                # path to get to goal.
                return self._parent_dict_to_path(parent_dict, start_vertex, v), None

            for w in neighbor_map[v]:
                if w in bfs_sequence:
                    continue
                bfs_sequence.append(w)
                parent_dict[w] = v
                processing_queue.append(w)

        # Goal was not found. The most useful information in this case is
        # bfs_sequence.
        return None, bfs_sequence

    def shortest_path(self, start_vertex: T, goal_vertex: T) -> deque[T] | None:
        path, _ = self.breadth_first_search(
            start_vertex, goal=lambda v: v == goal_vertex
        )
        return path

    def is_connected(self) -> Literal[True] | list[Graph[T]]:
        if not self.vertices:
            return True  # Empty graph is vacuously connected.
        start_vertex, *_ = self.vertices

        def goal_to_force_full_exploration(_: T) -> bool:
            return False

        path, bfs_sequence = self.breadth_first_search(
            start_vertex, goal_to_force_full_exploration
        )
        assert path is None
        assert bfs_sequence
        if len(bfs_sequence) == len(self.vertices):
            return True
        return False
