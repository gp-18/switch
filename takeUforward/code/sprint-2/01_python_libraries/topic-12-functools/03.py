# Write recursive Fibonacci and add lru_cache memoization.

# Example 1:
# Input: fib(10)
# Output: 55 (computed in O(n) calls with @lru_cache)

# Example 2:
# Input: fib(30)
# Output: 832040

from functools import lru_cache

@lru_cache(maxsize=None)
def fib(n):
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)

print(f"fib(10) = {fib(10)}")
print(f"fib(30) = {fib(30)}")
