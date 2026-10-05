# You need to cache results of a recursive function. Which functools feature would you use?

# Example 1:
# Input: Requirement: Memoize expensive recursive calls like Fibonacci or DP
# Output: functools.lru_cache (or functools.cache in Python 3.9+)

# Example 2:
# Input: @lru_cache(maxsize=None)
# Output: Automatically stores function return values for identical arguments

from functools import lru_cache

# Answer: functools.lru_cache (or functools.cache)
@lru_cache(maxsize=None)
def fib(n):
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)

print(f"fib(10) = {fib(10)}")
