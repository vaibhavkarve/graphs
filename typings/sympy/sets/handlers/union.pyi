"""
This type stub file was generated by pyright.
"""

from sympy.sets.sets import EmptySet, FiniteSet, Interval, ProductSet, Set, UniversalSet
from sympy.sets.fancysets import ComplexRegion, Integers, Naturals, Naturals0, Rationals, Reals

union_sets = ...
@union_sets.register(Naturals0, Naturals)
def _(a, b):
    ...

@union_sets.register(Rationals, Naturals)
def _(a, b):
    ...

@union_sets.register(Rationals, Naturals0)
def _(a, b):
    ...

@union_sets.register(Reals, Naturals)
def _(a, b):
    ...

@union_sets.register(Reals, Naturals0)
def _(a, b):
    ...

@union_sets.register(Reals, Rationals)
def _(a, b):
    ...

@union_sets.register(Integers, Set)
def _(a, b): # -> None:
    ...

@union_sets.register(ComplexRegion, Set)
def _(a, b): # -> FiniteSet | Set | None:
    ...

@union_sets.register(EmptySet, Set)
def _(a, b):
    ...

@union_sets.register(UniversalSet, Set)
def _(a, b):
    ...

@union_sets.register(ProductSet, ProductSet)
def _(a, b): # -> None:
    ...

@union_sets.register(ProductSet, Set)
def _(a, b): # -> None:
    ...

@union_sets.register(Interval, Interval)
def _(a, b): # -> FiniteSet | Interval | None:
    ...

@union_sets.register(Interval, UniversalSet)
def _(a, b):
    ...

@union_sets.register(Interval, Set)
def _(a, b): # -> set[Any | FiniteSet | Interval] | None:
    ...

@union_sets.register(FiniteSet, FiniteSet)
def _(a, b): # -> FiniteSet:
    ...

@union_sets.register(FiniteSet, Set)
def _(a, b): # -> set[Any | FiniteSet] | None:
    ...

@union_sets.register(Set, Set)
def _(a, b): # -> None:
    ...

