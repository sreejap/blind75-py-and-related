# example
def factorial(n):
    if n == 0: return 1
    return n * factorial(n-1)

# fibonacci
def fib(n):
    if n <= 1: return n
    return fib(n-1) + fib(n-2)

# lru_cache for memoization

from functools import lru_cache

@lru_cache(None)
def fib(n):
    if n <= 1: return n
    return fib(n-1) + fib(n-2)
