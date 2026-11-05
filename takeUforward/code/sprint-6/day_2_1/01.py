# Find Square Root of a Number (Floor Sqrt)
# Given a non-negative integer n, find and return its square root.
# If n is not a perfect square, return the floor value of sqrt(n).
#
# Example 1:
# Input:  n = 36
# Output: 6
#
# Example 2:
# Input:  n = 28
# Output: 5
#
# Example 3:
# Input:  n = 50
# Output: 7
#
# Think About:
# - Search space: low = 0, high = n.
# - If mid * mid <= n: mid is a valid candidate for floor sqrt; search right (low = mid + 1).
# - Else: mid * mid > n, search left (high = mid - 1).
# - When low > high, high holds the largest integer whose square is <= n.
# - Time Complexity: O(log n)
# - Space Complexity: O(1) auxiliary space
#

n = int(input("Enter non-negative integer n : "))

print(f"Finding floor square root for n = {n}...")

# Write your solution below:
# Optimal Approach: Binary Search on Answer Space [0, n]
# Time Complexity: O(log n) | Space Complexity: O(1)

low = 0
high = n
ans = 0

while low <= high:
    mid = low + (high - low) // 2
    value = mid * mid

    if value <= n:
        ans = mid
        # Try finding a larger integer whose square is still <= n
        low = mid + 1
    else:
        # mid^2 is too large, eliminate right half
        high = mid - 1

print(f"The floor square root of {n} is : {ans}")
