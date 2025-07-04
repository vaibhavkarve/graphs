"""
This type stub file was generated by pyright.
"""

'''Functions returning normal forms of matrices'''
def smith_normal_form(m, domain=...): # -> MutableDenseMatrix:
    '''
    Return the Smith Normal Form of a matrix `m` over the ring `domain`.
    This will only work if the ring is a principal ideal domain.

    Examples
    ========

    >>> from sympy import Matrix, ZZ
    >>> from sympy.matrices.normalforms import smith_normal_form
    >>> m = Matrix([[12, 6, 4], [3, 9, 6], [2, 16, 14]])
    >>> print(smith_normal_form(m, domain=ZZ))
    Matrix([[1, 0, 0], [0, 10, 0], [0, 0, 30]])

    '''
    ...

def is_smith_normal_form(m, domain=...): # -> bool:
    '''
    Checks that the matrix is in Smith Normal Form
    '''
    ...

def smith_normal_decomp(m, domain=...): # -> tuple[MutableDenseMatrix, MutableDenseMatrix, MutableDenseMatrix]:
    '''
    Return the Smith Normal Decomposition of a matrix `m` over the ring
    `domain`. This will only work if the ring is a principal ideal domain.

    Examples
    ========

    >>> from sympy import Matrix, ZZ
    >>> from sympy.matrices.normalforms import smith_normal_decomp
    >>> m = Matrix([[12, 6, 4], [3, 9, 6], [2, 16, 14]])
    >>> a, s, t = smith_normal_decomp(m, domain=ZZ)
    >>> assert a == s * m * t
    '''
    ...

def invariant_factors(m, domain=...): # -> tuple[Poly, ...] | tuple[Any, ...]:
    '''
    Return the tuple of abelian invariants for a matrix `m`
    (as in the Smith-Normal form)

    References
    ==========

    .. [1] https://en.wikipedia.org/wiki/Smith_normal_form#Algorithm
    .. [2] https://web.archive.org/web/20200331143852/https://sierra.nmsu.edu/morandi/notes/SmithNormalForm.pdf

    '''
    ...

def hermite_normal_form(A, *, D=..., check_rank=...): # -> MutableDenseMatrix:
    r"""
    Compute the Hermite Normal Form of a Matrix *A* of integers.

    Examples
    ========

    >>> from sympy import Matrix
    >>> from sympy.matrices.normalforms import hermite_normal_form
    >>> m = Matrix([[12, 6, 4], [3, 9, 6], [2, 16, 14]])
    >>> print(hermite_normal_form(m))
    Matrix([[10, 0, 2], [0, 15, 3], [0, 0, 2]])

    Parameters
    ==========

    A : $m \times n$ ``Matrix`` of integers.

    D : int, optional
        Let $W$ be the HNF of *A*. If known in advance, a positive integer *D*
        being any multiple of $\det(W)$ may be provided. In this case, if *A*
        also has rank $m$, then we may use an alternative algorithm that works
        mod *D* in order to prevent coefficient explosion.

    check_rank : boolean, optional (default=False)
        The basic assumption is that, if you pass a value for *D*, then
        you already believe that *A* has rank $m$, so we do not waste time
        checking it for you. If you do want this to be checked (and the
        ordinary, non-modulo *D* algorithm to be used if the check fails), then
        set *check_rank* to ``True``.

    Returns
    =======

    ``Matrix``
        The HNF of matrix *A*.

    Raises
    ======

    DMDomainError
        If the domain of the matrix is not :ref:`ZZ`.

    DMShapeError
        If the mod *D* algorithm is used but the matrix has more rows than
        columns.

    References
    ==========

    .. [1] Cohen, H. *A Course in Computational Algebraic Number Theory.*
       (See Algorithms 2.4.5 and 2.4.8.)

    """
    ...

