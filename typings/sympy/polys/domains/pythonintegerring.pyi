"""
This type stub file was generated by pyright.
"""

from sympy.polys.domains.groundtypes import PythonInteger
from sympy.polys.domains.integerring import IntegerRing
from sympy.utilities import public

"""Implementation of :class:`PythonIntegerRing` class. """
@public
class PythonIntegerRing(IntegerRing):
    """Integer ring based on Python's ``int`` type.

    This will be used as :ref:`ZZ` if ``gmpy`` and ``gmpy2`` are not
    installed. Elements are instances of the standard Python ``int`` type.
    """
    dtype = PythonInteger
    zero = ...
    one = ...
    alias = ...
    def __init__(self) -> None:
        """Allow instantiation of this domain. """
        ...
    
    def to_sympy(self, a): # -> One | NegativeOne | Zero | Integer:
        """Convert ``a`` to a SymPy object. """
        ...
    
    def from_sympy(self, a): # -> int:
        """Convert SymPy's Integer to ``dtype``. """
        ...
    
    def from_FF_python(K1, a, K0):
        """Convert ``ModularInteger(int)`` to Python's ``int``. """
        ...
    
    def from_ZZ_python(K1, a, K0):
        """Convert Python's ``int`` to Python's ``int``. """
        ...
    
    def from_QQ(K1, a, K0): # -> None:
        """Convert Python's ``Fraction`` to Python's ``int``. """
        ...
    
    def from_QQ_python(K1, a, K0): # -> None:
        """Convert Python's ``Fraction`` to Python's ``int``. """
        ...
    
    def from_FF_gmpy(K1, a, K0): # -> int:
        """Convert ``ModularInteger(mpz)`` to Python's ``int``. """
        ...
    
    def from_ZZ_gmpy(K1, a, K0): # -> int:
        """Convert GMPY's ``mpz`` to Python's ``int``. """
        ...
    
    def from_QQ_gmpy(K1, a, K0): # -> int | None:
        """Convert GMPY's ``mpq`` to Python's ``int``. """
        ...
    
    def from_RealField(K1, a, K0): # -> int | None:
        """Convert mpmath's ``mpf`` to Python's ``int``. """
        ...
    
    def gcdex(self, a, b): # -> tuple[int | Any, int | Any, int | Any]:
        """Compute extended GCD of ``a`` and ``b``. """
        ...
    
    def gcd(self, a, b): # -> int:
        """Compute GCD of ``a`` and ``b``. """
        ...
    
    def lcm(self, a, b): # -> int:
        """Compute LCM of ``a`` and ``b``. """
        ...
    
    def sqrt(self, a):
        """Compute square root of ``a``. """
        ...
    
    def factorial(self, a): # -> int:
        """Compute factorial of ``a``. """
        ...
    


