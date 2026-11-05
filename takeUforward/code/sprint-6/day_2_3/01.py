# Find the Smallest Divisor Given a Threshold
# Given an array of integers nums and an integer limit as the threshold value.
# Find the smallest positive integer divisor such that the sum of the division
# results (rounded up using ceiling) is <= limit.
#
# Example 1:
# Input:  nums = [1, 2, 3, 4, 5], limit = 8
# Output: 3
#
# Example 2:
# Input:  nums = [8, 4, 2, 3], limit = 10
# Output: 2
#
# Example 3:
# Input:  nums = [8, 4, 2, 3], limit = 4
# Output: 8
#
# Think About:
# - Search space: low = 1, high = max(nums).
# - As divisor increases, total sum monotonically decreases.
# - If total_sum <= limit: mid is a valid divisor, search left (high = mid - 1) to minimize.
# - Else: search right (low = mid + 1).
# - Ceiling division without floats: (num + divisor - 1) // divisor.
# - Time Complexity: O(N * log(max(nums)))
# - Space Complexity: O(1) auxiliary space
#

length = int(input("Enter the length of the array : "))
array = []

for i in range(length):
    value = int(input(f"Enter the value to insert at index {i} : "))
    array.append(value)

limit = int(input("Enter the threshold limit : "))

print(f"Your array : {array} with threshold limit = {limit}")

# Write your solution below:
# Optimal Approach: Binary Search on Answers [1, max(nums)]
# Time Complexity: O(N * log(max(nums))) | Space Complexity: O(1)

def compute_sum(nums, divisor):
    total = 0
    for x in nums:
        # Integer formula for ceil(x / divisor): (x + divisor - 1) // divisor
        total += (x + divisor - 1) // divisor
    return total

if length > limit:
    print("Array length is greater than threshold limit. Impossible (returned -1).")
else:
    low = 1
    high = max(array)
    ans = high

    while low <= high:
        mid = low + (high - low) // 2
        sum_val = compute_sum(array, mid)

        if sum_val <= limit:
            ans = mid
            # Try to find a smaller valid divisor on the left
            high = mid - 1
        else:
            # Sum is too large, need a larger divisor
            low = mid + 1

    print(f"The smallest divisor is : {ans}")
