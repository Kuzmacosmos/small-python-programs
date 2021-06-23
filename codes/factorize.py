# Version 1.1
from typing import List
"""A small python program of integer prime factorization, 
written by myself for python practice.
Code might be somewhat buggy and I will update it sometimes..."""
def factor(num: int) -> List[int]:
    """Return a list containing the prime factors of a (positive) integer num.
    Precondition: num > 0
    >>> factor(10)
    [2, 5]
    >>> factor(15)
    [3, 5]
    >>> factor(20)
    [2, 2, 5]
    """
    result = []
    i = 2
    while i <= num:
        if num % i == 0:
            result.append(i)
            num //= i
        else:
            i += 1
    return result
# I plan to write a function returning a dictionary later times.

def find_prime(n_i: int, n_f: int) -> List[int]:
    """Return a list containing prime integers ranging from two integers: n_i to n_f, inclusive.
    
    >>> find_prime(2, 5)
    [2, 3, 5]
    >>> find_prime(10, 100)
    [11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    """
    
    result = []
    for i in range(n_i, n_f + 1):
        if len(factor(i)) == 1:
            result.append(i)
    return result
