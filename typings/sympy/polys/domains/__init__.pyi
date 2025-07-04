"""
This type stub file was generated by pyright.
"""

from .domain import Domain
from .finitefield import FF, FiniteField, GF
from .integerring import IntegerRing, ZZ
from .rationalfield import QQ, RationalField
from .algebraicfield import AlgebraicField
from .gaussiandomains import QQ_I, ZZ_I
from .realfield import RR, RealField
from .complexfield import CC, ComplexField
from .polynomialring import PolynomialRing
from .fractionfield import FractionField
from .expressiondomain import EX, ExpressionDomain
from .expressionrawdomain import EXRAW
from .pythonrational import PythonRational
from sympy.external.gmpy import GROUND_TYPES
from .pythonfinitefield import PythonFiniteField
from .gmpyfinitefield import GMPYFiniteField
from .pythonintegerring import PythonIntegerRing
from .gmpyintegerring import GMPYIntegerRing
from .pythonrationalfield import PythonRationalField
from .gmpyrationalfield import GMPYRationalField

"""Implementation of mathematical domains. """
__all__ = ['Domain', 'FiniteField', 'IntegerRing', 'RationalField', 'RealField', 'ComplexField', 'AlgebraicField', 'PolynomialRing', 'FractionField', 'ExpressionDomain', 'PythonRational', 'GF', 'FF', 'ZZ', 'QQ', 'ZZ_I', 'QQ_I', 'RR', 'CC', 'EX', 'EXRAW']
FF_python = PythonFiniteField
FF_gmpy = GMPYFiniteField
ZZ_python = PythonIntegerRing
ZZ_gmpy = GMPYIntegerRing
QQ_python = PythonRationalField
QQ_gmpy = GMPYRationalField
