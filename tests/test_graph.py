import itertools as it
from math import comb
from typing import TYPE_CHECKING, Final

import more_itertools as mit
import pytest
from hypothesis import given
from hypothesis import strategies as st
from sympy.sets.sets import EmptySet, FiniteSet

from graphs.exceptions import EdgeSizeError, NotInVertexSetError
from graphs.generator import complete_graph
from graphs.graph import Graph
from graphs.symgraph import SymGraph


if TYPE_CHECKING:
    from collections import deque


MIN_VERTEX_VALUE: Final[int] = 0
MAX_VERTEX_VALUE: Final[int] = 10


def int_vertices() -> st.SearchStrategy[frozenset[int]]:
    return st.frozensets(
        st.integers(min_value=MIN_VERTEX_VALUE, max_value=MAX_VERTEX_VALUE),
    )


def int_edges() -> st.SearchStrategy[frozenset[frozenset[int]]]:
    return st.frozensets(
        st.frozensets(
            st.integers(min_value=MIN_VERTEX_VALUE, max_value=MAX_VERTEX_VALUE),
            min_size=Graph.EDGE_SIZE,
            max_size=Graph.EDGE_SIZE,
        )
    )


@st.composite
def int_graphs(draw: st.DrawFn) -> Graph[int]:
    edges: frozenset[frozenset[int]] = draw(int_edges())
    vertices: frozenset[int] = draw(int_vertices()) | frozenset(mit.flatten(edges))
    return Graph(edges=edges, vertices=vertices)


st.register_type_strategy(Graph, int_graphs())


def symgraphs() -> st.SearchStrategy[SymGraph[int]]:
    return st.builds(
        SymGraph[int].from_edgeset,
        edges=st.builds(FiniteSet[int], st.builds(FiniteSet[int], st.integers())),
    )


@given(int_graphs())
def test_graph(g: Graph[int]) -> None:
    assert g
    assert g != SymGraph(EmptySet(), EmptySet())
    assert g != (frozenset(), frozenset(frozenset()))  # pyright: ignore[reportUnknownArgumentType]


@given(int_graphs())
def test_graph_not_in_vertex_set_error(g: Graph[int]) -> None:
    extra_edge: tuple[int, int] = (MAX_VERTEX_VALUE, MAX_VERTEX_VALUE + 1)
    with pytest.raises(NotInVertexSetError):
        Graph(vertices=g.vertices, edges=g.edges | frozenset([extra_edge]))


@given(int_graphs().filter(lambda g: len(g.vertices) >= Graph.EDGE_SIZE + 1))
def test_graph_edge_size_error(g: Graph[int]) -> None:
    u, *_ = g.vertices
    short_edge: tuple[int] = (u,)
    with pytest.raises(EdgeSizeError):
        Graph(vertices=g.vertices, edges=g.edges | frozenset([short_edge]))

    u, v, w, *_ = g.vertices
    long_edge: tuple[int, int, int] = (u, v, w)
    with pytest.raises(EdgeSizeError):
        Graph(vertices=g.vertices, edges=g.edges | frozenset([long_edge]))


@given(int_graphs())
def test_roundtrip_graph_neighbor_map_graph_from_neighbor_map(g: Graph[int]) -> None:
    nmap: dict[int, frozenset[int]] = g.neighbor_map()
    g2: Graph[int] = Graph[int].from_neighbor_map(nmap)
    assert g == g2, f"{g = }, {nmap = }, {g2 = }"


@given(st.integers(min_value=MIN_VERTEX_VALUE, max_value=MAX_VERTEX_VALUE))
def test_complete_graph(n: int) -> None:
    k_n: Graph[int] = complete_graph(n)
    assert mit.ilen(k_n.vertices) == n
    assert mit.ilen(k_n.edges) == comb(n, 2)
    assert k_n.components()


@given(int_graphs().filter(lambda g: g.vertices and g.is_connected()))
def test_shortest_path(g: Graph[int]) -> None:
    start_vertex: int = min(g.vertices)
    goal_vertex: int = max(g.vertices)
    path: deque[int] | None = g.shortest_path(start_vertex, goal_vertex)

    assert path

    assert path[0] == start_vertex
    assert path[-1] == goal_vertex
    for v, w in it.pairwise(path):
        assert frozenset({v, w}) in g.edges


@given(int_graphs().filter(lambda g: g.is_connected()))
def test_components_assume_connected(g: Graph[int]) -> None:
    components: list[Graph[int]] = list(g.components())
    assert len(components) == 1
    assert components[0] == g


@given(int_graphs().filter(lambda g: not g.is_connected()))
def test_components_assume_disconnected(g: Graph[int]) -> None:
    components: list[Graph[int]] = list(g.components())

    if not g.vertices:
        # This must be the empty graph.
        assert not g.edges
        assert not components
        return  # Early exit.

    assert len(components) > 1
    assert set().union(*[c.vertices for c in components]) == g.vertices
    assert set().union(*[c.edges for c in components]) == g.edges
    for c in components:
        c_components = list(c.components())
        assert len(c_components) == 1
        assert c_components[0] == c


def test_symgraph() -> None:
    SymGraph(EmptySet(), EmptySet())
    SymGraph(FiniteSet(1, 2, 3), EmptySet())
    SymGraph(FiniteSet(1, 2, 3), FiniteSet(FiniteSet(1, 2), FiniteSet(2, 3)))
