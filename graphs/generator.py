import itertools as it

from graphs.graph import Graph


def complete_graph(n: int) -> Graph[int]:
    return Graph(range(n), it.combinations(range(n), 2))
