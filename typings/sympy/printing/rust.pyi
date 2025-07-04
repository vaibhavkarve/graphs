"""
This type stub file was generated by pyright.
"""

from typing import Any
from sympy.core.expr import Expr
from sympy.functions.elementary.integers import ceiling, floor
from sympy.printing.codeprinter import CodePrinter

"""
Rust code printer

The `RustCodePrinter` converts SymPy expressions into Rust expressions.

A complete code generator, which uses `rust_code` extensively, can be found
in `sympy.utilities.codegen`. The `codegen` module can be used to generate
complete source code files.

"""
class float_floor(floor):
    """
    Same as `sympy.floor`, but mimics the Rust behavior of returning a float rather than an integer
    """
    ...


class float_ceiling(ceiling):
    """
    Same as `sympy.ceiling`, but mimics the Rust behavior of returning a float rather than an integer
    """
    ...


function_overrides = ...
known_functions = ...
reserved_words = ...
class TypeCast(Expr):
    """
    The type casting operator of the Rust language.
    """
    def __init__(self, expr, type_) -> None:
        ...
    
    @property
    def expr(self): # -> Basic:
        ...
    
    @property
    def type_(self): # -> Basic:
        ...
    
    def sort_key(self, order=...): # -> tuple[tuple[int, int, str], tuple[int, tuple[tuple[tuple[int, int, str], Any, tuple[tuple[Literal[1], Literal[0], Literal['Number']], tuple[int, tuple[()]], tuple[()], One], One], ...]], tuple[tuple[Literal[1], Literal[0], Literal['Number']], tuple[int, tuple[()]], tuple[()], One], One]:
        ...
    


class RustCodePrinter(CodePrinter):
    """A printer to convert SymPy expressions to strings of Rust code"""
    printmethod = ...
    language = ...
    type_aliases = ...
    type_mappings = ...
    _default_settings: dict[str, Any] = ...
    def __init__(self, settings=...) -> None:
        ...
    
    def indent_code(self, code): # -> str | list[Any]:
        """Accepts a string of code or a list of code lines"""
        ...
    


