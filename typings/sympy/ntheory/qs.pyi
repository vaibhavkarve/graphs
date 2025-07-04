"""
This type stub file was generated by pyright.
"""

class SievePolynomial:
    def __init__(self, a, b, N) -> None:
        """This class denotes the sieve polynomial.
        Provide methods to compute `(a*x + b)**2 - N` and
        `a*x + b` when given `x`.

        Parameters
        ==========

        a : parameter of the sieve polynomial
        b : parameter of the sieve polynomial
        N : number to be factored

        """
        ...
    
    def eval_u(self, x):
        ...
    
    def eval_v(self, x):
        ...
    


class FactorBaseElem:
    """This class stores an element of the `factor_base`.
    """
    def __init__(self, prime, tmem_p, log_p) -> None:
        """
        Initialization of factor_base_elem.

        Parameters
        ==========

        prime : prime number of the factor_base
        tmem_p : Integer square root of x**2 = n mod prime
        log_p : Compute Natural Logarithm of the prime
        """
        ...
    


def qs(N, prime_bound, M, ERROR_TERM=..., seed=...): # -> set[Any]:
    """Performs factorization using Self-Initializing Quadratic Sieve.
    In SIQS, let N be a number to be factored, and this N should not be a
    perfect power. If we find two integers such that ``X**2 = Y**2 modN`` and
    ``X != +-Y modN``, then `gcd(X + Y, N)` will reveal a proper factor of N.
    In order to find these integers X and Y we try to find relations of form
    t**2 = u modN where u is a product of small primes. If we have enough of
    these relations then we can form ``(t1*t2...ti)**2 = u1*u2...ui modN`` such that
    the right hand side is a square, thus we found a relation of ``X**2 = Y**2 modN``.

    Here, several optimizations are done like using multiple polynomials for
    sieving, fast changing between polynomials and using partial relations.
    The use of partial relations can speeds up the factoring by 2 times.

    Parameters
    ==========

    N : Number to be Factored
    prime_bound : upper bound for primes in the factor base
    M : Sieve Interval
    ERROR_TERM : Error term for checking smoothness
    seed : seed of random number generator

    Returns
    =======

    set(int) : A set of factors of N without considering multiplicity.
               Returns ``{N}`` if factorization fails.

    Examples
    ========

    >>> from sympy.ntheory import qs
    >>> qs(25645121643901801, 2000, 10000)
    {5394769, 4753701529}
    >>> qs(9804659461513846513, 2000, 10000)
    {4641991, 2112166839943}

    See Also
    ========

    qs_factor

    References
    ==========

    .. [1] https://pdfs.semanticscholar.org/5c52/8a975c1405bd35c65993abf5a4edb667c1db.pdf
    .. [2] https://www.rieselprime.de/ziki/Self-initializing_quadratic_sieve
    """
    ...

def qs_factor(N, prime_bound, M, ERROR_TERM=..., seed=...): # -> dict[Any, Any]:
    """ Performs factorization using Self-Initializing Quadratic Sieve.

    Parameters
    ==========

    N : Number to be Factored
    prime_bound : upper bound for primes in the factor base
    M : Sieve Interval
    ERROR_TERM : Error term for checking smoothness
    seed : seed of random number generator

    Returns
    =======

    dict[int, int] : Factors of N.
                     Returns ``{N: 1}`` if factorization fails.
                     Note that the key is not always a prime number.

    Examples
    ========

    >>> from sympy.ntheory import qs_factor
    >>> qs_factor(1009 * 100003, 2000, 10000)
    {1009: 1, 100003: 1}

    See Also
    ========

    qs

    """
    ...

