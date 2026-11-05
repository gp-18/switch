# Find Nth Root of a Number
# Given two numbers N and M, find the Nth root of M.
# Return integer X such that X^N = M.
# If no such integer exists, return -1.
#
# Example 1:
# Input:  N = 3, M = 27
# Output: 3
#
# Example 2:
# Input:  N = 4, M = 69
# Output: -1
#
# Example 3:
# Input:  N = 4, M = 81
# Output: 3
#
# Think About:
# - Search space: low = 1, high = M.
# - Use helper function with exponentiation by squaring to prevent overflow:
#     returns 1 if mid^N == M
#     returns 0 if mid^N < M
#     returns 2 if mid^N > M (early exit as soon as running product > M)
# - Time Complexity: O(log M * log N)
# - Space Complexity: O(1) auxiliary space
#

N = int(input("Enter power N : "))
M = int(input("Enter target value M : "))

print(f"Finding {N}-th root of {M}...")

# Write your solution below:
# Optimal Approach: Binary Search on [1, M] with Exponentiation by Squaring
# Time Complexity: O(log M * log N) | Space Complexity: O(1)

def power_check(mid, n, m):
    """
    Computes mid^n with early exit:
    Returns:
      1 if mid^n == m
      0 if mid^n < m
      2 if mid^n > m
    """
    ans = 1
    base = mid

    while n > 0:
        if n % 2 == 1:
            ans *= base
            if ans > m:
                return 2  # Exceeded m early
            n -= 1
        else:
            n //= 2
            base *= base
            if base > m and n > 0:
                return 2

    if ans == m:
        return 1
    return 0

low = 1
high = M
root = -1

while low <= high:
    mid = low + (high - low) // 2
    status = power_check(mid, N, M)

    if status == 1:
        root = mid
        break
    elif status == 0:
        # mid^N < M, search right
        low = mid + 1
    else:
        # mid^N > M, search left
        high = mid - 1

if root == -1:
    print(f"The {N}-th root of {M} is not an integer (returned -1).")
else:
    print(f"The {N}-th root of {M} is : {root}")
