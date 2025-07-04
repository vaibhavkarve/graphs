"""
This type stub file was generated by pyright.
"""

from .sympify import SympifyError, sympify
from .cache import cacheit
from .assumptions import assumptions, check_assumptions, common_assumptions, failing_assumptions
from .basic import Atom, Basic
from .singleton import S
from .expr import AtomicExpr, Expr, UnevaluatedExpr
from .symbol import Dummy, Symbol, Wild, symbols, var
from .numbers import AlgebraicNumber, E, Float, I, Integer, Number, NumberSymbol, Rational, RealNumber, comp, igcd, ilcm, mod_inverse, nan, oo, pi, seterr, zoo
from .power import Pow
from .intfunc import integer_log, integer_nthroot, num_digits, trailing
from .mul import Mul, prod
from .add import Add
from .mod import Mod
from .relational import Eq, Equality, Ge, GreaterThan, Gt, Le, LessThan, Lt, Ne, Rel, StrictGreaterThan, StrictLessThan, Unequality
from .multidimensional import vectorize
from .function import Derivative, Function, FunctionClass, Lambda, PoleError, Subs, WildFunction, arity, count_ops, diff, expand, expand_complex, expand_func, expand_log, expand_mul, expand_multinomial, expand_power_base, expand_power_exp, expand_trig, nfloat
from .evalf import N, PrecisionExhausted
from .containers import Dict, Tuple
from .exprtools import factor_nc, factor_terms, gcd_terms
from .parameters import evaluate
from .kind import BooleanKind, NumberKind, UndefinedKind
from .traversal import bottom_up, postorder_traversal, preorder_traversal, use
from .sorting import default_sort_key, ordered

"""Core module. Provides the basic operations needed in sympy.
"""
Catalan = ...
EulerGamma = ...
GoldenRatio = ...
TribonacciConstant = ...
__all__ = ['sympify', 'SympifyError', 'cacheit', 'assumptions', 'check_assumptions', 'failing_assumptions', 'common_assumptions', 'Basic', 'Atom', 'S', 'Expr', 'AtomicExpr', 'UnevaluatedExpr', 'Symbol', 'Wild', 'Dummy', 'symbols', 'var', 'Number', 'Float', 'Rational', 'Integer', 'NumberSymbol', 'RealNumber', 'igcd', 'ilcm', 'seterr', 'E', 'I', 'nan', 'oo', 'pi', 'zoo', 'AlgebraicNumber', 'comp', 'mod_inverse', 'Pow', 'integer_nthroot', 'integer_log', 'num_digits', 'trailing', 'Mul', 'prod', 'Add', 'Mod', 'Rel', 'Eq', 'Ne', 'Lt', 'Le', 'Gt', 'Ge', 'Equality', 'GreaterThan', 'LessThan', 'Unequality', 'StrictGreaterThan', 'StrictLessThan', 'vectorize', 'Lambda', 'WildFunction', 'Derivative', 'diff', 'FunctionClass', 'Function', 'Subs', 'expand', 'PoleError', 'count_ops', 'expand_mul', 'expand_log', 'expand_func', 'expand_trig', 'expand_complex', 'expand_multinomial', 'nfloat', 'expand_power_base', 'expand_power_exp', 'arity', 'PrecisionExhausted', 'N', 'evalf', 'Tuple', 'Dict', 'gcd_terms', 'factor_terms', 'factor_nc', 'evaluate', 'Catalan', 'EulerGamma', 'GoldenRatio', 'TribonacciConstant', 'UndefinedKind', 'NumberKind', 'BooleanKind', 'preorder_traversal', 'bottom_up', 'use', 'postorder_traversal', 'default_sort_key', 'ordered']
